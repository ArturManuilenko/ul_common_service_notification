from unipipeline.brokers.uni_amqp_py_broker import UniAmqpPyBroker

from src.conf.notification_service_input_worker import NOTIFICATION__AMQP_BROKER__URI


class DefaultAmqpBroker(UniAmqpPyBroker):

    @classmethod
    def get_connection_uri(cls) -> str:
        return NOTIFICATION__AMQP_BROKER__URI
