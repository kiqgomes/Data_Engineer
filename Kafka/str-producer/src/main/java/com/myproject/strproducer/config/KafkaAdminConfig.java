package com.myproject.strproducer.config;

import java.util.HashMap;

import org.apache.kafka.clients.admin.AdminClientConfig;
import org.springframework.boot.autoconfigure.kafka.KafkaProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.kafka.config.TopicBuilder;
import org.springframework.kafka.core.KafkaAdmin;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@Configuration // Annotation to set a configuration
/**
 * KafkaAdminConfig
 */
public class KafkaAdminConfig {

    public final KafkaProperties properties; // Setting the properties using the annotation '@RequiredArgsConstructor'

    @Bean // Ups our method always that run
    public KafkaAdmin kafkaAdmin() { // Configuring a kafka admin to connect to our kafka service  
        var configs = new HashMap<String,Object>();
        configs.put(AdminClientConfig.BOOTSTRAP_SERVERS_CONFIG,properties.getBootstrapServers());
        return new KafkaAdmin(configs);
    }

    // Creating a topic
    @Bean
    public KafkaAdmin.NewTopics topics(){
        return new KafkaAdmin.NewTopics(
            TopicBuilder.name("str-topic").partitions(2).replicas(1).build()
        );
    }
}