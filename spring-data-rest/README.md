# OUGN 2017 - P78, P77

This application is based on spring guide: https://spring.io/guides/gs/accessing-data-rest/

Read that guide to learn more.

If you are using Maven, you can run the application using ```./mvnw spring-boot:run```.

Or you can build the JAR file with ```./mvnw clean package```. Then you can run the JAR file:

```java -jar target/ougn-2017-p78-rest-application-0.1.0.jar ```

This application is configured to go against an external database thru application.properties
```
#Basic Spring Boot Config for Oracle
spring.datasource.url= jdbc:oracle:thin:@localhost:49161/XE
spring.datasource.username=sandbox
spring.datasource.password=sandbox
spring.datasource.driver-class-name=oracle.jdbc.OracleDriver

#hibernate config
spring.jpa.database-platform=org.hibernate.dialect.Oracle10gDialect
spring.jpa.generate-ddl=true

logging.level.org.springframework.web=WARN
logging.level.org.hibernate=ERROR
```
If you want to use h2 database delete spring.* properties in the config file.
