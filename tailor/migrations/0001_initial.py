# Generated by Django 3.0.7 on 2020-08-15 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('checkbox', models.BooleanField(null=True)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=30)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tailor.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('price', models.FloatField()),
                ('digital', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=30)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('zipcode', models.CharField(blank=True, max_length=30)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tailor.Customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tailor.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tailor.Order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tailor.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Male',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chest', models.CharField(blank=True, max_length=30)),
                ('neck', models.CharField(blank=True, max_length=30)),
                ('full_shoulder_width', models.CharField(blank=True, max_length=30)),
                ('right_sleeve', models.CharField(blank=True, max_length=30)),
                ('left_sleeve', models.CharField(blank=True, max_length=30)),
                ('bicep', models.CharField(blank=True, max_length=30)),
                ('shoulder_width', models.CharField(blank=True, max_length=30)),
                ('seat', models.CharField(blank=True, max_length=30)),
                ('arm_length', models.CharField(blank=True, max_length=30)),
                ('thigh', models.CharField(blank=True, max_length=30)),
                ('waist', models.CharField(blank=True, max_length=30)),
                ('wrist', models.CharField(blank=True, max_length=30)),
                ('hip', models.CharField(blank=True, max_length=30)),
                ('full_back_length', models.CharField(blank=True, max_length=30)),
                ('front_chest_width', models.CharField(blank=True, max_length=30)),
                ('contact1', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='tailor.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Female',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fchest', models.CharField(blank=True, max_length=30)),
                ('fneck', models.CharField(blank=True, max_length=30)),
                ('fwaist', models.CharField(blank=True, max_length=30)),
                ('seat', models.CharField(blank=True, max_length=30)),
                ('shoulder_width', models.CharField(blank=True, max_length=30)),
                ('arm_length', models.CharField(blank=True, max_length=30)),
                ('hip', models.CharField(blank=True, max_length=30)),
                ('biceps', models.CharField(blank=True, max_length=30)),
                ('back_length', models.CharField(blank=True, max_length=30)),
                ('wrist', models.CharField(blank=True, max_length=30)),
                ('sleeve_length', models.CharField(blank=True, max_length=30)),
                ('arm_hole', models.CharField(blank=True, max_length=30)),
                ('bust', models.CharField(blank=True, max_length=30)),
                ('upper_bust', models.CharField(blank=True, max_length=30)),
                ('skirt_length', models.CharField(blank=True, max_length=30)),
                ('shoulder_to_shoulder', models.CharField(blank=True, max_length=30)),
                ('full_back_length', models.CharField(blank=True, max_length=30)),
                ('contact2', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='tailor.Contact')),
            ],
        ),
    ]
