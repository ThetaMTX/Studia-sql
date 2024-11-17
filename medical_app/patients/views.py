from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, Examination
from .forms import PatientForm, ExaminationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages


@login_required
def patient_list(request):
    sort_by = request.GET.get('sort', 'last_name')  # Default sorting by first name
    if sort_by == 'first_name':
        patients = Patient.objects.all().order_by('first_name')
    elif sort_by == 'date_of_birth':
        patients = Patient.objects.all().order_by('date_of_birth')
    else:
        patients = Patient.objects.all().order_by('last_name')

    return render(request, 'patients/patient_list.html', {'patients': patients})


@login_required
def examination_list(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    sort_by = request.GET.get('sort', 'date')  # Default sorting by date
    if sort_by == 'description':
        examinations = patient.examinations.all().order_by('description')
    else:
        examinations = patient.examinations.all().order_by('date')

    return render(request, 'patients/examination_list.html', {'patient': patient, 'examinations': examinations})


@login_required
def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})


@login_required
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')  # Redirect to the patient list after saving
    else:
        form = PatientForm(instance=patient)

    return render(request, 'patients/edit_patient.html', {'form': form, 'patient': patient})


@login_required
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient has been successfully deleted.')
        return redirect(reverse('patient_list'))




@login_required
def add_examination(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = ExaminationForm(request.POST, request.FILES)
        if form.is_valid():
            examination = form.save(commit=False)
            examination.patient = patient
            examination.save()
            return redirect('examination_list', pk=patient.pk)
    else:
        form = ExaminationForm()
    return render(request, 'patients/add_examination.html', {'form': form, 'patient': patient})


@login_required
def delete_examination(request, patient_pk, exam_pk):
    patient = get_object_or_404(Patient, pk=patient_pk)
    examination = get_object_or_404(Examination, pk=exam_pk)

    if request.method == 'POST':
        examination.delete()
        return redirect('examination_list', pk=patient.pk)  # Redirect to the examination list

    return render(request, 'patients/delete_examination.html', {'examination': examination})


@login_required
def delete_patient_confirmation(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patients/patient_confirm_delete.html', {'patient': patient})


@login_required
def edit_examination(request, examination_pk, patient_pk):
    examination = get_object_or_404(Examination, pk=examination_pk)
    patient = get_object_or_404(Patient, pk=patient_pk)

    if request.method == 'POST':
        form = ExaminationForm(request.POST, request.FILES, instance=examination)
        if form.is_valid():
            form.save()
            return redirect('examination_list', pk=patient.pk)
    else:
        form = ExaminationForm(instance=examination)

    return render(request, 'patients/edit_examination.html',
                  {'form': form, 'patient': patient, 'examination': examination})
