from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Attendance


@login_required
def mark_attendance(request):
    today = timezone.now().date()
    attendance, created = Attendance.objects.get_or_create(employee=request.user, date=today)

    if request.method == 'POST':
        selfie = request.FILES.get('selfie')
        action = request.POST.get('action')

        if action == 'check_in':
            attendance.check_in = timezone.now().time()
            attendance.check_in_selfie = selfie
            attendance.status = 'present'
            attendance.save()
            messages.success(request, 'Checked in successfully!')

        elif action == 'check_out':
            attendance.check_out = timezone.now().time()
            attendance.check_out_selfie = selfie
            attendance.save()
            messages.success(request, 'Checked out successfully!')

        return redirect('mark_attendance')

    return render(request, 'attendance/mark_attendance.html', {'attendance': attendance})

@login_required
def view_attendance(request):
    if request.user.role != 'admin':
        return redirect('employee_dashboard')

    today = timezone.now().date()
    attendances = Attendance.objects.filter(date=today).select_related('employee')

    return render(request, 'attendance/view_attendance.html', {
        'attendances': attendances,
        'today': today,
    })