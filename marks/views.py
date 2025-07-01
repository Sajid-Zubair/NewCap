from django.shortcuts import render
from .models import *
from collections import defaultdict

def fetch_marks_table(request):
    if request.method == 'POST':
        regulation_id = request.POST.get('regulation')
        exam_type_id = request.POST.get('exam_type')
        year = request.POST.get('year')
        semester = request.POST.get('semester')
        branch_id = request.POST.get('branch')
        section_id = request.POST.get('section')

        exam_type = ExamType.objects.get(id=exam_type_id)

        students = Student.objects.filter(
            regulation_id=regulation_id,
            branch_id=branch_id,
            section_id=section_id,
            semester=semester
        )

        offerings = SubjectOffering.objects.filter(
            regulation_id=regulation_id,
            branch_id=branch_id,
            semester=semester
        ).select_related('subject')

        subjects = [o.subject for o in offerings]

        marks = Marks.objects.filter(
            student__in=students,
            subject__in=subjects,
            exam_type_id=exam_type_id
        ).select_related('student', 'subject')

        student_marks = defaultdict(lambda: defaultdict(str))

        for mark in marks:
            student_marks[mark.student.roll_number][mark.subject.name] = mark.marks_obtained

        final_rows = []
        for student in students:
            row = {
                'student_id': student.roll_number,
                'student_name': student.name
            }
            for subject in subjects:
                row[subject.name] = student_marks[student.roll_number].get(subject.name, '-')
            final_rows.append(row)
        
        print("Students:", students.count())
        print("Offerings:", offerings.count())
        print("Subjects:", subjects)
        print("Marks:", marks.count())
        print(f"Rows: {final_rows}")
        print(f"Subjects: {[s.name for s in subjects]}")

        return render(request, 'marks/marks_table.html', {
            'rows': final_rows,
            'subjects': [s.name for s in subjects],
            'exam_type_name': exam_type.name
        })

    context = {
        'regulations': Regulation.objects.all(),
        'exam_types': ExamType.objects.all(),
        'branches': Branch.objects.all(),
        'sections': Section.objects.all(),
    }
    return render(request, 'marks/marks_form.html', context)
