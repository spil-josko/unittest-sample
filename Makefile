# =============================================================================
# CONFIGURATION
# =============================================================================
APP=unittest-sample
PROJECT-TYPE=python
CONTAINER_VOLUMES=-v $(PWD) \
	-v $(PWD)/volumes/spil-bi-online-prd.json:/opt/container/secret.json \
	-v $(PWD)/test:/opt/container/test 
CONTAINER_ENVS=-e GOOGLE_CLOUD_PROJECT=spil-bi-online-stg \
	-e GOOGLE_CLOUD_DISABLE_GRPC=true \
	-e GOOGLE_APPLICATION_CREDENTIALS=/opt/secrets/service-account/spil-bi-online-prd.json \
	-e IMPORTER_GCS_PROJECT_NAME=spil-bi-online-stg \
	-e IMPORTER_GCS_BUCKET_NAME=spil-gc-etls-stg \
	-e IMPORTER_BQ_DATASET_NAME=raw__historized__staging__importers \
	-e LOG_TO_CONSOLE=true \
	-e HOST=devbox 

BUILD_CREDENTIALS=true
USE_JENKINS_UP=false
# =============================================================================
# COMMON TARGETS BELOW
# =============================================================================

.ME-test=off
.ME-k8s-up=normal
.ME-unittest=off

# =============================================================================
# DON'T UPDATE SECTION BELOW
# =============================================================================

# Include common makefile
-include microservices-ext/make/Makefile-common.mk

# Or get it, if it's not there
GITURL:="https://github.com/spilgames"
$(.ME-ext)microservices-ext:
	git clone -q $(GITURL)/microservices-ext
	-@test "`grep microservices-ext .gitignore`" || echo "microservices-ext/" >> .gitignore
	@make $(MAKECMDGOALS)
# =============================================================================
# PROJECT SPECIFIC TARGETS
# =============================================================================

test::  customtest pep8

customtest:
	docker run -t -v $(PWD)/test:/opt/container/test --entrypoint=/opt/container/test/test.sh  $(CONTAINER_VOLUMES) $(CONTAINER_ENVS) $(APP):latest
