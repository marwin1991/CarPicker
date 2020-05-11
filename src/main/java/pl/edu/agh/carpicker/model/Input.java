package pl.edu.agh.carpicker.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;


@Setter
@Getter
@NoArgsConstructor
@AllArgsConstructor
public class Input {

    private int enginePower; //KM
    private double fuelUsage; //l/100km
    private double acceleration; //0-100km in how much seconds
    private int maxSpeed; //km/h
    private int engineReliability = 5; // in scale from 1 to 10

    private int carFrontSpace; //1-10
    private int carBackSpace;// 1-10
    private int trunkSpace; // l
    private int comfort = 5; // in scale from 1 to 10

    private String job;
    private String savingAccounts;
    private String checkingAccounts;

    private int creditAmount;
    private int duration;
    private String purpose;
}
