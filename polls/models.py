import secrets
import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Poll(models.Model):
    """
    Model representing a poll.

    This model represents a poll with fields such as 'owner' (ForeignKey to User model),
    'text' (TextField for the poll question), 'pub_date' (DateTimeField for the publication
    date), and 'active' (BooleanField to indicate if the poll is active or not). It also
    defines methods to check if a user can vote, get the vote count, and get the result
    dictionary for the poll.

    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def user_can_vote(self, user):
        """ 
        Return False if user already voted.
        """
        user_votes = user.vote_set.all()
        qs = user_votes.filter(poll=self)
        if qs.exists():
            return False
        return True

    @property
    def get_vote_count(self):
        return self.vote_set.count()

    def get_result_dict(self):
    res = []
    for choice in self.choice_set.all():
        d = {}
        alert_class = ['primary', 'secondary', 'success',
                       'danger', 'dark', 'warning', 'info']

        d['alert_class'] = secrets.choice(alert_class)
        d['text'] = choice.choice_text
        d['num_votes'] = choice.get_vote_count
        if not self.get_vote_count():
            d['percentage'] = 0
        else:
            d['percentage'] = (choice.get_vote_count /
                               self.get_vote_count) * 100

        res.append(d)
    return res



class Choice(models.Model):
    """
    Model representing a choice in a poll.

    This model represents a choice in a poll, with a ForeignKey relationship to the
    Poll model. It has a 'choice_text' field (CharField for the choice text), and a
    method to get the vote count for the choice.

    """
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)

    @property
    def get_vote_count(self):
        return self.vote_set.count()

    def __str__(self):
        return f"{self.poll.text[:25]} - {self.choice_text[:25]}"


class Vote(models.Model):
    """
    Model representing a vote in a poll.

    This model represents a vote in a poll, with ForeignKey relationships to the User,
    Poll, and Choice models. It does not define any methods.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.poll.text[:15]} - {self.choice.choice_text[:15]} - {self.user.username}'

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        