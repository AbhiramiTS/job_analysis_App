import os
import django
from collections import defaultdict

# Step 1: Set the environment variable to point to your Django project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_analysis.settings')  
# Step 2: Initialize Django
django.setup()

from app.models import (
    Company,
    CompanyIndustry,
    CompanySpeciality,
    CompanyMetrics,
    Salary,
    JobSkill,
    JobIndustry,
    Skill,
    Industry
)

def remove_duplicates(queryset, unique_fields):
    duplicates = defaultdict(list)
    for obj in queryset:
        key = tuple(getattr(obj, field) for field in unique_fields)  # Create a unique key based on specified fields
        duplicates[key].append(obj)

    # Prepare to delete duplicates, keeping the first occurrence
    duplicates_to_delete = []
    for key, instances in duplicates.items():
        if len(instances) > 1:  # More than one duplicate found
            duplicates_to_delete.extend(instances[1:])  # Keep the first instance, delete the rest

    # Delete duplicates in batches
    batch_size = 900  # Safe batch size for SQLite
    if duplicates_to_delete:
        for i in range(0, len(duplicates_to_delete), batch_size):
            batch = duplicates_to_delete[i:i + batch_size]
            queryset.filter(pk__in=[obj.pk for obj in batch]).delete()
        print(f"Deleted {len(duplicates_to_delete)} duplicates.")
    else:
        print("No duplicates found.")

# 1. Remove duplicates from Company
remove_duplicates(Company.objects.all(), ['name', 'url'])

# 2. Remove duplicates from CompanyIndustry
remove_duplicates(CompanyIndustry.objects.all(), ['company', 'industry'])

# 3. Remove duplicates from CompanySpeciality
remove_duplicates(CompanySpeciality.objects.all(), ['company', 'speciality'])

# 4. Remove duplicates from CompanyMetrics
remove_duplicates(CompanyMetrics.objects.all(), ['company', 'time_recorded'])

# 5. Remove duplicates from Salary
remove_duplicates(Salary.objects.all(), ['job', 'pay_period', 'currency'])

# 6. Remove duplicates from JobSkill
remove_duplicates(JobSkill.objects.all(), ['job', 'skill_abr'])

# 7. Remove duplicates from JobIndustry
remove_duplicates(JobIndustry.objects.all(), ['job', 'industry'])

# 8. Remove duplicates from Skill
remove_duplicates(Skill.objects.all(), ['skill_abr'])

# 10. Remove duplicates from Industry
remove_duplicates(Industry.objects.all(), ['industry_name'])
