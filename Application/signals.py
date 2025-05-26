from django.db.models.signals import pre_save
from django.dispatch import receiver

from Application.models import RealEstate, AgentRealEstate


@receiver(pre_save, sender=RealEstate)
def handle_saving_house(sender, instance, **kwargs):
    old_instance = RealEstate.objects.filter(id=instance.id).first()

    if old_instance:
        if old_instance.sold != instance.sold:
            agents_real_estate = AgentRealEstate.objects.filter(realestate = old_instance).all()
            for agent in agents_real_estate:
                agent = agent.agent
                agent.total_sales += 1
                agent.save()