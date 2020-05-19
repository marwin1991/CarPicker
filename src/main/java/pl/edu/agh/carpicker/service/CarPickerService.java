package pl.edu.agh.carpicker.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pl.edu.agh.carpicker.model.Input;
import pl.edu.agh.carpicker.model.Result;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

@Slf4j
@Service
public class CarPickerService {

    @Autowired
    private ObjectMapper objectMapper;

    public Result process(Input input) throws JsonProcessingException {
        String command = "python .\\python\\main.py " + getArgs(input);
        log.info("Command: " + command);
        StringBuilder out = new StringBuilder();
        String s;
        String lastLine = "";
        try {
            Process p = Runtime.getRuntime().exec(command);

            BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
            BufferedReader stdError = new BufferedReader(new InputStreamReader(p.getErrorStream()));

            // read the output from the command
            System.out.println("Here is the standard output of the command:\n");

            while ((s = stdInput.readLine()) != null) {
                log.info(s);
                out.append("\n").append(s);
                lastLine = s;
            }

            // read any errors from the attempted command
            System.out.println("Here is the standard error of the command (if any):\n");
            while ((s = stdError.readLine()) != null) {
                log.error(s);
                //out.append("\n").append(s);
            }
        }
        catch (IOException e) {
            log.error(e.getMessage(), e);
        }

        String toParse = lastLine.replace("'", "\"");
        log.info(toParse);
        return objectMapper.readValue(toParse, Result.class);
    }

    private String getArgs(Input input){
        return input.getEnginePower() + " " +
                input.getFuelUsage() + " " +
                input.getAcceleration() + " " +
                input.getMaxSpeed() + " " +
                input.getEngineReliability() + " " +
                input.getCarFrontSpace() + " " +
                input.getCarBackSpace() + " " +
                input.getTrunkSpace() + " " +
                input.getComfort() + " " +
                input.getFinishQuality() + " " +
                input.getMuteQuality() + " " +
                input.getEaseOfUse() + " " +
                input.getComfortAdditionalEquipment() + " " +
                input.getSafetyAdditionalEquipment() + " " +
                input.getOtherAdditionalEquipment() + " " +
                input.getPrice() + " " +
                input.getPriceDef() + " " +
                input.getAdditionalCosts() + " " +
                input.getDrivingExpQuality() + " " +
                input.getBreaksQuality() + " " +
                input.getDrivingModes() + " " +
                input.getTransmission();

    }

}
