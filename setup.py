from setuptools import setup


setup(name='notify-run-server',
      version='0.0.6',
      python_requires='>=2.7',
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
          'PyQRCode==1.2.1',
          'cryptography>=2.5.0',
          'requests>=2.21.0',
          'Flask==1.0.2',
          'Flask-Cors==3.0.3',
          'SQLAlchemy>=1.3.0',
          'pywebpush==1.10.0',
          'setuptools>=41.0.1',
      ],
      )
