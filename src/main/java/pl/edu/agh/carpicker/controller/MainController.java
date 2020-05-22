package pl.edu.agh.carpicker.controller;

import com.fasterxml.jackson.core.JsonProcessingException;
import lombok.Getter;
import lombok.Setter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import pl.edu.agh.carpicker.model.Input;
import pl.edu.agh.carpicker.model.Rate;
import pl.edu.agh.carpicker.model.Result;
import pl.edu.agh.carpicker.repository.CarRateRepository;
import pl.edu.agh.carpicker.service.CarPickerService;

import java.util.LinkedList;


@Getter
@Setter
@Controller
public class MainController {

    private Input input = new Input();

    private Result result;

    private CarPickerService carPickerService;

    private CarRateRepository carRateRepository;

    @Autowired
    public MainController(CarPickerService carPickerService, CarRateRepository carRateRepository) {
        this.carPickerService = carPickerService;
        this.carRateRepository = carRateRepository;
    }

    @GetMapping("/")
    public String index(Model model) {
        this.input = new Input();
        this.result = null;
        prepareModel(model);
        return "index";
    }

    @PostMapping("/calculate")
    public String route(Model model, @ModelAttribute("input") Input input) throws JsonProcessingException {
        this.input = input;
        this.result = carPickerService.process(input);

        Rate rate = new Rate();
        LinkedList<Integer> r = new LinkedList<>();
        this.result.getCars().forEach(c -> r.add(0));
        rate.setRates(r);
        model.addAttribute("rate", rate);

        prepareModel(model);
        return "index";
    }

    @PostMapping("/rate")
    public String rate(Model model, @ModelAttribute("rate") Rate rate) {
        carRateRepository.saveRates(this.result, rate);
        prepareModel(model);
        return "thanks";
    }

    private void prepareModel(Model model){
        model.addAttribute("input", this.input);
        model.addAttribute("result", this.result);
    }
}
