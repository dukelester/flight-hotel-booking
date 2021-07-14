from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import  receiver
from django.utils import timezone
from sendgrid import Mail, SendGridAPIClient


from .models import MarkettingEmail, EmailSubscribers
from userprofile.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('user created')


post_save.connect(create_profile,sender=User)



from django.core.signals import request_finished


@receiver(post_save,sender=MarkettingEmail)
def email_sender(sender,instance,**kwargs):


    Email_subscribers = EmailSubscribers.objects.all()

    print(Email_subscribers)


    msg = MarkettingEmail.objects.latest('email')



    print('wasetdryfgyuhmsg',msg)
    print(MarkettingEmail.thistime)


    ms = msg.email
    print(ms)





    for email_subscriber in Email_subscribers:
        email = email_subscriber.email








        message = Mail(
            from_email='campaigns@sky-swift.com',
            to_emails=email,
            subject='Newsletter subscription',
            html_content=ms,

        )

        try:
            sg = SendGridAPIClient('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')
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)

        except Exception as e:
            print('not working')


post_save.connect(email_sender,sender=MarkettingEmail)







