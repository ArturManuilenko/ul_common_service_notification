SHELL := /bin/bash
CWD := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
ME := $(shell whoami)

nothing:
	@echo "do nothing"

up:
	docker-compose up --remove-orphans --build \
		notification__balancer \
		notification__broker__amqp \
		notification__api \
		notification__email_worker \
		notification__web \

check_env:
	@./srv/check_env.sh

cleanup:
	docker login gitlab.neroelectronics.by:5050 -u unic_lab_developers -p Vw3o4gBzgH_GGUzFs7NM

	@# git submodule foreach "git fetch && git merge origin/dev"
	git submodule init
	git submodule update --remote
	pipenv sync --dev

	ulpytool install

lint:
	pipenv run lint

tests:
	pipenv run test

drop:
	docker-compose down -v

fix_own:
	@echo "me: $(ME)"
	sudo chown $(ME):$(ME) -R .

######################## MANAGER NOTIFICATION DB START ########################

notification__db__dump:
	docker-compose run --rm manager__notification__db uldbutls dump '--db-uri=$$NOTIFICATION__DB_URI'

notification__db__migrate:
	docker-compose run --rm manager__notification__db uldbutls migrate --app-dir="./src/notification__db"

notification__db__revision:
	docker-compose run --rm manager__notification__db uldbutls revision --app-dir="./src/notification__db"

notification__db__init:
	docker-compose run --rm manager__notification__db uldbutls init --app-dir="./src/notification__db"

notification__db__upgrade:
	docker-compose run --rm manager__notification__db uldbutls upgrade --app-dir="./src/notification__db"

notification__db__downgrade:
	docker-compose run --rm manager__notification__db uldbutls downgrade --app-dir="./src/notification__db"

######################## MANAGER NOTIFICATION DB END ##########################
