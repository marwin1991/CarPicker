package pl.edu.agh.carpicker.service;

import com.jcabi.ssh.Shell;
import com.jcabi.ssh.Ssh;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import pl.edu.agh.carpicker.model.Input;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

@Slf4j
@Service
public class CarPickerService {

    public String process(Input input) {
        String command = "python .\\python\\main.py";
        StringBuilder out = new StringBuilder();
        String s;

        try {
            Process p = Runtime.getRuntime().exec(command);

            BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
            BufferedReader stdError = new BufferedReader(new InputStreamReader(p.getErrorStream()));

            // read the output from the command
            System.out.println("Here is the standard output of the command:\n");
            while ((s = stdInput.readLine()) != null) {
                log.info(s);
                out.append("\n").append(s);
            }

            // read any errors from the attempted command
            System.out.println("Here is the standard error of the command (if any):\n");
            while ((s = stdError.readLine()) != null) {
                log.error(s);
                out.append("\n").append(s);
            }
        }
        catch (IOException e) {
            log.error(e.getMessage(), e);
        }

        return out.toString();
    }

}
