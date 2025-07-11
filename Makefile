HTML_COV_DIR=htmlcov
COV_REPORT_FILE=coverage-report.txt
COV_REPORT_BASELINE_FILE=coverage-report-baseline.txt
COV_REPORT_CUR_BRANCH_FILE=coverage-report-$(shell basename $(shell git rev-parse --abbrev-ref HEAD)).txt
COV_REPORT_DIR=coverage-reports


COV_STAMP=.cov_stamp
TOX_STAMP=.tox_stamp
HTML_REPORT_STAMP=".html_report_stamp"

# find all *.py and *.json files under mq_randomizer
MQ_RANDOMIZER_SRC_FILES=$(shell find ./mq_randomizer -name \*\.py -print -o -name \*\.json -print)
# find all regular files under tests excluding *.pyc, and reports/
# this should include *.py, *.json, *.txt plus files without extensions
MQ_RANDOMIZER_TEST_FILES=$(shell find tests -name \*\.pyc -prune -o  -name reports -prune -o -type f -print)

all:
	@echo "make pytest-coverage for coverage report"

pytest-coverage: $(HTML_REPORT_STAMP)

tox: $(TOX_STAMP)

$(HTML_REPORT_STAMP): $(COV_STAMP)
	coverage html
	touch $@

coverage-report: $(COV_REPORT_FILE)

$(COV_REPORT_FILE): $(COV_STAMP)
	coverage report > $(COV_REPORT_FILE)

coverage-report-branch: $(COV_REPORT_FILE)
	mv $(COV_REPORT_FILE) $(COV_REPORT_CUR_BRANCH_FILE)

$(COV_REPORT_DIR):
	mkdir $@

coverage-report-baseline: $(COV_REPORT_BASELINE_FILE)

$(COV_REPORT_BASELINE_FILE): $(COV_REPORT_FILE) $(COV_REPORT_DIR)
	mv $(COV_REPORT_FILE) $(COV_REPORT_DIR)/$@

$(COV_STAMP): $(MQ_RANDOMIZER_SRC_FILES) $(MQ_RANDOMIZER_TEST_FILES)
	# not strictly necessary to erase previous coverage but stale
	# coverage can result in errors in some cases
	# see https://coverage.readthedocs.io/en/latest/faq.html
	coverage erase
	pytest --cov=mq_randomizer --cov-report= -n auto
	touch $@

$(TOX_STAMP): $(MQ_RANDOMIZER_SRC_FILES) $(MQ_RANDOMIZER_TEST_FILES)
	# run tox in parallel mode, recreating tox environment every time
	tox p -r
	touch $@

clean-coverage:
	-coverage erase
	-rm -r $(HTML_COV_DIR)
	-rm $(COV_STAMP)
	-rm $(HTML_REPORT_STAMP)
	-rm $(COV_REPORT_FILE)

clean: clean-coverage
	-rm -r .*cache
	-rm -r .tox*
	-rm -r build
	-rm -r .ipynb_checkpoints
	-rm -r *egg-info
