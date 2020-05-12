package pl.edu.agh.carpicker.controller;

import lombok.Getter;
import lombok.Setter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import pl.edu.agh.carpicker.model.Input;
import pl.edu.agh.carpicker.service.CarPickerService;

import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

@Getter
@Setter
@Controller
public class MainController {

    private Input input;

    private CarPickerService carPickerService;

    @Autowired
    public MainController(CarPickerService carPickerService) {
        this.carPickerService = carPickerService;
    }

    @GetMapping("/")
    public String index(Model model) {
        model.addAttribute("input", new Input());
        return "index";
    }

    @PostMapping("/calculate")
    public String route(Model model, @ModelAttribute("input") Input input) {
        this.input = input;
        model.addAttribute("result", carPickerService.test());
        return "index";
    }
}
