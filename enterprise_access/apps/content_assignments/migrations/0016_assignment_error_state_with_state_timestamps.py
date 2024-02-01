# Generated by Django 3.2.21 on 2024-01-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_assignments', '0015_learnercontentassignment_batch_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicallearnercontentassignment',
            name='last_notification_at',
        ),
        migrations.RemoveField(
            model_name='learnercontentassignment',
            name='last_notification_at',
        ),
        migrations.AddField(
            model_name='historicallearnercontentassignment',
            name='accepted_at',
            field=models.DateTimeField(blank=True, help_text='The last time this assignment was accepted. Null means the assignment is not accepted.', null=True),
        ),
        migrations.AddField(
            model_name='historicallearnercontentassignment',
            name='allocated_at',
            field=models.DateTimeField(blank=True, help_text='The last time the assignment was allocated. Null means the assignment is not allocated.', null=True),
        ),
        migrations.AddField(
            model_name='historicallearnercontentassignment',
            name='cancelled_at',
            field=models.DateTimeField(blank=True, help_text='The last time this assignment was cancelled. Null means the assignment is not cancelled.', null=True),
        ),
        migrations.AddField(
            model_name='historicallearnercontentassignment',
            name='errored_at',
            field=models.DateTimeField(blank=True, help_text='The last time this assignment was in an error state. Null means the assignment is not errored.', null=True),
        ),
        migrations.AddField(
            model_name='historicallearnercontentassignment',
            name='expired_at',
            field=models.DateTimeField(blank=True, help_text='The last time this assignment was expired. Null means the assignment is not expired.', null=True),
        ),
        migrations.AddField(
            model_name='learnercontentassignment',
            name='accepted_at',
            field=models.DateTimeField(blank=True, help_text='The last time this assignment was accepted. Null means the assignment is not accepted.', null=True),
        ),
        migrations.AddField(
            model_name='learnercontentassignment',
            name='allocated_at',
            field=models.DateTimeField(blank=True, help_text='The last time the assignment was allocated. Null means the assignment is not allocated.', null=True),
        ),
        migrations.AddField(
            model_name='learnercontentassignment',
            name='cancelled_at',
            field=models.DateTimeField(blank=True, help_text='The last time this assignment was cancelled. Null means the assignment is not cancelled.', null=True),
        ),
        migrations.AddField(
            model_name='learnercontentassignment',
            name='errored_at',
            field=models.DateTimeField(blank=True, help_text='The last time this assignment was in an error state. Null means the assignment is not errored.', null=True),
        ),
        migrations.AddField(
            model_name='learnercontentassignment',
            name='expired_at',
            field=models.DateTimeField(blank=True, help_text='The last time this assignment was expired. Null means the assignment is not expired.', null=True),
        ),
        migrations.AlterField(
            model_name='historicallearnercontentassignment',
            name='state',
            field=models.CharField(choices=[('allocated', 'Allocated'), ('accepted', 'Accepted'), ('cancelled', 'Cancelled'), ('errored', 'Errored'), ('expired', 'Expired')], db_index=True, default='allocated', help_text="The current state of the LearnerContentAssignment. One of: ['allocated', 'accepted', 'cancelled', 'errored', 'expired']", max_length=255),
        ),
        migrations.AlterField(
            model_name='historicallearnercontentassignmentaction',
            name='action_type',
            field=models.CharField(choices=[('learner_linked', 'Learner linked to customer'), ('notified', 'Learner notified of assignment'), ('reminded', 'Learner reminded about assignment'), ('redeemed', 'Learner redeemed the assigned content'), ('cancelled', 'Learner assignment cancelled'), ('automatic_cancellation', 'Learner assignment cancelled automatically'), ('expired', 'Learner assignment expired')], db_index=True, help_text='The type of action take on the related assignment record.', max_length=255),
        ),
        migrations.AlterField(
            model_name='learnercontentassignment',
            name='state',
            field=models.CharField(choices=[('allocated', 'Allocated'), ('accepted', 'Accepted'), ('cancelled', 'Cancelled'), ('errored', 'Errored'), ('expired', 'Expired')], db_index=True, default='allocated', help_text="The current state of the LearnerContentAssignment. One of: ['allocated', 'accepted', 'cancelled', 'errored', 'expired']", max_length=255),
        ),
        migrations.AlterField(
            model_name='learnercontentassignmentaction',
            name='action_type',
            field=models.CharField(choices=[('learner_linked', 'Learner linked to customer'), ('notified', 'Learner notified of assignment'), ('reminded', 'Learner reminded about assignment'), ('redeemed', 'Learner redeemed the assigned content'), ('cancelled', 'Learner assignment cancelled'), ('automatic_cancellation', 'Learner assignment cancelled automatically'), ('expired', 'Learner assignment expired')], db_index=True, help_text='The type of action take on the related assignment record.', max_length=255),
        ),
    ]