# Let's get this party started!
from wsgiref.simple_server import make_server

import falcon
import sys
import logging

logging.basicConfig(format='[%(asctime)s] [%(threadName)s] [%(levelname)s] %(message)s', level=logging.INFO)


class PingResource:
    def on_get(self, req, resp):
        logging.info('Received ping request')
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = ('\nPong\n')


class FibonacciResource:
    def fibonacci(self, n):
        sequence = []
        a, b = 0, 1
        while len(sequence) < n:
            a, b = b, a + b
            sequence.append(a)
        return sequence

    def on_get(self, req, resp, num):
        logging.info('Received Fibonacci request for %s', num)
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        logging.info('Returning >>>' + str(self.fibonacci(num)) + '<<<')
        resp.text = str(self.fibonacci(num))


# falcon.App instances are callable WSGI apps
# in larger applications the app is created in a separate file
app = falcon.App()
logging.info("Running Python version %s", sys.version_info[0])

# Resources are represented by long-lived class instances
ping = PingResource()
fibonacci = FibonacciResource()

# things will handle all requests to the '/things' URL path
app.add_route('/api/ping', ping)
app.add_route('/api/fibonacci/{num:int}', fibonacci)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()
