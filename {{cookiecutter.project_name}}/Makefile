REGISTRY = arvintian
PROJECT = code-dist-api
VERSION = 1.0.0

package:
	docker build -t $(REGISTRY)/$(PROJECT):$(VERSION) .

publish:
	docker push $(REGISTRY)/$(PROJECT):$(VERSION)

clean:
	docker images | grep -E "$(PROJECT)" | awk '{print $$3}' | uniq | xargs -I {} docker rmi --force {}