# Usage: after installing requirements and running migrations, run:
# python load_sample_data.py
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','online_crime_monitoring.settings')
import django
django.setup()
from django.contrib.auth.models import User
from crimeapp.models import CrimeReport

def run():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin','admin@example.com','admin123')
        print('Created admin/admin123')
    if not User.objects.filter(username='citizen1').exists():
        u = User.objects.create_user('citizen1','c1@example.com','pass123')
        print('Created citizen1/pass123')
        CrimeReport.objects.create(user=u, title='Robbery at Market Road', description='Robbery occurred near Market Road at 8pm.', location='Market Road', status='Pending')
        CrimeReport.objects.create(user=u, title='Cyber fraud report', description='Received fraudulent messages asking for bank details.', location='Online', status='In Progress')
        print('Created sample reports for citizen1')

if __name__ == '__main__':
    run()
