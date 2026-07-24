from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import CustomUser
from .models import Payroll

@login_required
def generate_payroll(request):
    if request.user.role != 'admin':
        return redirect('employee_dashboard')

    employees = CustomUser.objects.filter(role='employee')

    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        month = int(request.POST.get('month'))
        year = int(request.POST.get('year'))
        basic_pay = float(request.POST.get('basic_pay'))
        allowances = float(request.POST.get('allowances') or 0)
        deductions = float(request.POST.get('deductions') or 0)

        employee = CustomUser.objects.get(id=employee_id)


        if Payroll.objects.filter(employee=employee, month=month, year=year).exists():
            messages.error(request, f'Payroll for {employee.username} already exists for this month!')
        else:
            Payroll.objects.create(
                employee=employee,
                month=month,
                year=year,
                basic_pay=basic_pay,
                allowances=allowances,
                deductions=deductions,
            )
            messages.success(request, 'Payroll generated successfully!')

        return redirect('generate_payroll')

    return render(request, 'payroll/generate_payroll.html', {'employees': employees})


@login_required
def payroll_list(request):
    if request.user.role != 'admin':
        return redirect('employee_dashboard')

    payrolls = Payroll.objects.all().select_related('employee')
    return render(request, 'payroll/payroll_list.html', {'payrolls': payrolls})

@login_required
def my_salary(request):
    payrolls = Payroll.objects.filter(employee=request.user)
    return render(request, 'payroll/my_salary.html', {'payrolls': payrolls})