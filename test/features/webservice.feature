Feature: requesting a data set upload responds with 200 OK
	Scenario: Requesting service on an endpoint
		Given I have a request to upload data
		When I request service on the endpoint
		Then I get a 200 OK response
