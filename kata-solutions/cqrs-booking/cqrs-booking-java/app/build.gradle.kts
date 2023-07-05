plugins {
    // Apply the application plugin to add support for building a CLI application in Java.
    application
}

repositories {
    // Use Maven Central for resolving dependencies.
    mavenCentral()
}

dependencies {
    // For rSpec-like syntax
    testImplementation("com.mscharhag.oleaster:oleaster-runner:0.2.0")
    testImplementation("com.mscharhag.oleaster:oleaster-matcher:0.2.0")
    
    // Use JUnit Jupiter API for testing.
    testImplementation("org.junit.jupiter:junit-jupiter-api:5.6.2")

    // Use JUnit Jupiter Engine for testing.
    testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine")

    // This dependency is used by the application.
    implementation("com.google.guava:guava:29.0-jre")

    // Added for CQRS
    implementation("org.axonframework:axon-spring-boot-starter:4.6.3")
    testImplementation("org.axonframework:axon-test:4.6.3")
}

application {
    // Define the main class for the application.
    mainClass.set("CqrsBooking")
}

tasks.test {
    // Use junit platform for unit tests.
    useJUnitPlatform()
    testLogging {
        events("PASSED", "SKIPPED", "FAILED", "STANDARD_OUT", "STANDARD_ERROR")
        showStandardStreams = true
    }  
}
