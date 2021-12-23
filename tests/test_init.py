import unittest

from aws_sqs_consumer import Consumer

class TestQueueURL(unittest.TestCase):
    def test_queue_url(self):
        class TestConsumer(Consumer):
            def handle_message(self, message):
                pass

        queue_url = "https://sqs.us-east-1.amazonaws.com/12345678901/test_queue"
        consumer = TestConsumer(queue_url)
        self.assertEqual(consumer.queue_url, queue_url)

if __name__ == '__main__':
    unittest.main()