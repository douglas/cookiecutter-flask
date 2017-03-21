all:
	@echo "To run the travis tests, use: make travis_test"

travis_test_pipenv:
	@rm -rf myflaskapp
	cookiecutter . --no-input
	$(MAKE) -C myflaskapp travis_test_pipenv
	rm -rf myflaskapp

travis_test:
	@rm -rf myflaskapp
	cookiecutter . --no-input
	$(MAKE) -C myflaskapp test
	rm -rf myflaskapp
