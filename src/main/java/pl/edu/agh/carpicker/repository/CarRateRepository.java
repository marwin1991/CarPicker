package pl.edu.agh.carpicker.repository;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.namedparam.MapSqlParameterSource;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.jdbc.core.namedparam.SqlParameterSource;
import org.springframework.stereotype.Repository;
import pl.edu.agh.carpicker.model.Rate;
import pl.edu.agh.carpicker.model.Result;

import javax.sql.DataSource;
import java.time.LocalDateTime;

@Slf4j
@Repository
public class CarRateRepository {

    private NamedParameterJdbcTemplate jdbcTemplate;

    @Autowired
    public CarRateRepository(DataSource dataSource) {
        this.jdbcTemplate = new NamedParameterJdbcTemplate(dataSource);
    }

    public void saveRates(Result result, Rate rate){
        for(int i = 0; i < result.getCars().size(); i++){
            String query = "INSERT INTO car_picker VALUES (current_timestamp, :engine, car_body, " +
                    ":cost, :car_details , :equipment, :driving_features, :car_name, :rate)";

            MapSqlParameterSource sqlParameterSource = new MapSqlParameterSource()
                    .addValue("engine", result.getFeatures().get(0))
                    .addValue("car_body", result.getFeatures().get(1))
                    .addValue("cost", result.getFeatures().get(2))
                    .addValue("car_details", result.getFeatures().get(3))
                    .addValue("equipment", result.getFeatures().get(4))
                    .addValue("driving_features", result.getFeatures().get(5))
                    .addValue("car_name", result.getCars().get(i).getName())
                    .addValue("rate", rate.getRates().get(i));

            jdbcTemplate.update(query, sqlParameterSource);
        }

    }
}
