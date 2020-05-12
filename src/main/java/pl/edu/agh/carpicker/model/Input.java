package pl.edu.agh.carpicker.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.math.BigDecimal;


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

    private int comfortAdditionalEquipment;
    private int safetyAdditionalEquipment;
    private int otherAdditionalEquipment;

    private BigDecimal price = BigDecimal.valueOf(100000L);
    private BigDecimal priceDef = BigDecimal.valueOf(80000L);
    private BigDecimal additionalCosts = BigDecimal.valueOf(5000);


    private int drivingExpQuality; //1-10
    private int breaksQuality;// 1-10
    private int transmission; //1-Manual, 5-All, 10-Auto
}
