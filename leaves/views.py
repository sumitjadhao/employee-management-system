from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Leave


@login_required
def apply_leave(request):
    if request.user.role != 'employee':
        return redirect('admin_dashboard')

    if request.method == 'POST':
        leave_type = request.POST.get('leave_type')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        reason = request.POST.get('reason')

        Leave.objects.create(
            employee=request.user,
            leave_type=leave_type,
            from_date=from_date,
            to_date=to_date,
            reason=reason,
        )
        messages.success(request, 'Leave request submitted successfully!')
        return redirect('apply_leave')

    my_leaves = Leave.objects.filter(employee=request.user)
    return render(request, 'leaves/apply_leave.html', {'my_leaves': my_leaves})


@login_required
def manage_leaves(request):
    if request.user.role != 'admin':
        return redirect('employee_dashboard')

    leaves = Leave.objects.all().select_related('employee')
    return render(request, 'leaves/manage_leaves.html', {'leaves': leaves})


@login_required
def update_leave_status(request, leave_id, new_status):
    if request.user.role != 'admin':
        return redirect('employee_dashboard')

    leave = get_object_or_404(Leave, id=leave_id)
    leave.status = new_status
    leave.save()
    messages.success(request, f'Leave request {new_status}!')
    return redirect('manage_leaves')