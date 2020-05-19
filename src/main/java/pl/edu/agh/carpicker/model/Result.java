package pl.edu.agh.carpicker.model;

import lombok.Data;

import java.util.List;

@Data
public class Result {
    private List<Car> cars;
    private List<Integer> features;
}
