__author__ = 'Patrick B. Grinaway'

from celery import Celery
import yaml
import os

config_file = open(os.environ['CELERY_CONFIG'], 'r')
config = yaml.load(config_file)
config_file.close()

app = Celery('hydration_energies',
             broker=config['broker'],
             backend=config['backend'],
             include=['hydration_energies.energytasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)



if __name__ == '__main__':
    app.start()


