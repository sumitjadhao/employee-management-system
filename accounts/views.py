from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EmployeeCreationForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('employee_dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def admin_dashboard(request):
    from django.utils import timezone
    from attendance.models import Attendance
    from leaves.models import Leave

    today = timezone.now().date()

    total_employees = CustomUser.objects.filter(role='employee').count()
    total_departments = CustomUser.objects.filter(role='employee').exclude(department__isnull=True).exclude(department='').values('department').distinct().count()
    present_today = Attendance.objects.filter(date=today, status='present').count()
    on_leave_today = Leave.objects.filter(status='approved', from_date__lte=today, to_date__gte=today).count()

    context = {
        'total_employees': total_employees,
        'total_departments': total_departments,
        'present_today': present_today,
        'on_leave_today': on_leave_today,
    }
    return render(request, 'accounts/admin_dashboard.html', context)


@login_required
def employee_dashboard(request):
    return render(request, 'accounts/employee_dashboard.html')


@login_required
def add_employee(request):
    if request.user.role != 'admin':
        return redirect('employee_dashboard')

    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee account created successfully!')
            return redirect('add_employee')
    else:
        form = EmployeeCreationForm()

    return render(request, 'accounts/add_employee.html', {'form': form})

@login_required
def employee_list(request):
    if request.user.role != 'admin':
        return redirect('employee_dashboard')

    employees = CustomUser.objects.filter(role='employee')
    return render(request, 'accounts/employee_list.html', {'employees': employees})



@login_required
def edit_employee(request, employee_id):
    if request.user.role != 'admin':
        return redirect('employee_dashboard')

    employee = get_object_or_404(CustomUser, id=employee_id, role='employee')

    if request.method == 'POST':
        employee.email = request.POST.get('email')
        employee.phone = request.POST.get('phone')
        employee.department = request.POST.get('department')
        employee.designation = request.POST.get('designation')
        employee.save()
        messages.success(request, 'Employee updated successfully!')
        return redirect('employee_list')

    return render(request, 'accounts/edit_employee.html', {'employee': employee})


@login_required
def delete_employee(request, employee_id):
    if request.user.role != 'admin':
        return redirect('employee_dashboard')

    employee = get_object_or_404(CustomUser, id=employee_id, role='employee')

    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully!')
        return redirect('employee_list')

    return render(request, 'accounts/delete_employee.html', {'employee': employee})