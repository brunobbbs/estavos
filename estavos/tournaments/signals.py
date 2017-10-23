from pagseguro.signals import notificacao_recebida
from estavos.tournaments.models import Payment, Inscription


def update_status(sender, transaction, **kwargs):
    code = transaction['code']
    payment_status = transaction['status']
    inscription = Inscription.objects.get(slug=transaction['reference'])

    try:
        obj = Payment.objects.get(transaction=code)
    except Payment.DoesNotExist:
        obj = Payment.objects.create(
            transaction=code,
        )
        inscription.payment = obj
        inscription.save()

    obj.status = payment_status
    if payment_status in ['3', '4']:
        inscription.confirmed = True
        inscription.save()
        obj.paid = True
    else:
        obj.paid = False

    obj.save()


notificacao_recebida.connect(update_status)
