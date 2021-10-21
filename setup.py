from setuptools import setup


setup(name='notify-run-server',
      version='0.0.7',
      python_requires='>=3.10',
      description='Server for self-hosted notify.run server.',
      author='Paul Butler',
      author_email='notify@paulbutler.org',
      url='https://notify.run/',
      packages=['notify_run_server'],
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'notify-run-server = notify_run_server.app:main'
          ]
      },
      install_requires=[
          'boto3>=1.19.0',
          'PyQRCode==1.2.1',
          'cryptography>=35.0.0',
          'requests>=2.21.0',
          'Flask>=2.0.2',
          'Flask-Cors>=3.0.10',
          'SQLAlchemy>=1.4.26',
          'pywebpush>=1.14.0',
          'setuptools>=58.2.0',
      ],
      )
