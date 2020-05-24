package pl.edu.agh.carpicker;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.sql.DataSource;

@Configuration
@SpringBootApplication
public class CarPickerApplication {

    public static void main(String[] args) {
        SpringApplication.run(CarPickerApplication.class, args);
    }

    @Bean
    public DataSource dataSource() {
        DataSourceBuilder dataSourceBuilder = DataSourceBuilder.create();
        dataSourceBuilder.driverClassName("org.sqlite.JDBC");
        dataSourceBuilder.url("jdbc:sqlite:car_rates.db");
        DataSource dataSource = dataSourceBuilder.build();

        JdbcTemplate jdbcTemplate = new JdbcTemplate(dataSource);
        jdbcTemplate.update(
                "CREATE TABLE IF NOT EXISTS car_rates " +
                "(dt datetime default current_timestamp, " +
                "engine real, " +
                "car_body real, " +
                "costs real, " +
                "car_details real, " +
                "equipment real, " +
                "driving_features real," +
                "car text, " +
                "grade real)");

        //jdbcTemplate.update("INSERT INTO car_rates VALUES (current_timestamp,51,71,61,81,41,31,'Audi A4', 5)");
        return dataSource;
    }
}
