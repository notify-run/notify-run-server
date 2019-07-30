cd notify-run-site

./build.sh

cd -

cp -r notify-run-site/public notify_run_server/static

python setup.py sdist

