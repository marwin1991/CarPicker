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

    private int enginePower = 120; //KM 1 - 400
    private double fuelUsage = 5.8; //l/100km
    private double acceleration = 4.7; //0-100km in how much seconds
    private int maxSpeed = 190; //km/h
    private int engineReliability = 5; // in scale from 1 to 10

    private int carFrontSpace = 5; //1-10
    private int carBackSpace = 5;// 1-10
    private int trunkSpace = 200; // l
    private int comfort = 5; // in scale from 1 to 10

    private int finishQuality = 5;
    private int muteQuality = 5;
    private int easeOfUse = 5;

    private int comfortAdditionalEquipment = 5;
    private int safetyAdditionalEquipment = 5;
    private int otherAdditionalEquipment = 5;

    private BigDecimal price = BigDecimal.valueOf(100000L);
    private BigDecimal priceDef = BigDecimal.valueOf(80000L);
    private BigDecimal additionalCosts = BigDecimal.valueOf(5000);


    private int drivingExpQuality = 5; //1-10
    private int breaksQuality = 5;// 1-10

    private int drivingModes = 5;
    private int transmission = 5; //1-Manual, 5-All, 10-Auto


    public int getEXTEnginePower() {
        return (enginePower * 10 / 400);
    }

    public int getEXTFuelUsage() {
        int f = (int) (fuelUsage * 10 / 25);
        return Math.min(f, 10);

    }

    public int getEXTAcceleration() {
        return (int) (acceleration * 10 / 25);
    }

    public int getEXTMaxSpeed() {
        return maxSpeed * 10 / 300;
    }

    public int getEXTEngineReliability() {
        return engineReliability;
    }

    public int getEXTCarFrontSpace() {
        return carFrontSpace;
    }

    public int getEXTCarBackSpace() {
        return carBackSpace;
    }

    public int getEXTTrunkSpace() {
        return trunkSpace * 10 / 500;
    }

    public int getEXTComfort() {
        return comfort;
    }

    public int getEXTFinishQuality() {
        return finishQuality;
    }

    public int getEXTMuteQuality() {
        return muteQuality;
    }

    public int getEXTEaseOfUse() {
        return easeOfUse;
    }

    public int getEXTComfortAdditionalEquipment() {
        return comfortAdditionalEquipment;
    }

    public int getEXTSafetyAdditionalEquipment() {
        return safetyAdditionalEquipment;
    }

    public int getEXTOtherAdditionalEquipment() {
        return otherAdditionalEquipment;
    }

    public int getEXTPrice() {
        return price.intValue() * 10 / 1000000;
    }

    public int getEXTPriceDef() {
        try {
            return priceDef.divide(price).intValue() * 10;
        } catch (Exception e) {
            return 0;
        }
    }

    public int getEXTAdditionalCosts() {
        try {
            return additionalCosts.divide(price).intValue() * 10;
        } catch (Exception e) {
            return 0;
        }
    }

    public int getEXTDrivingExpQuality() {
        return drivingExpQuality;
    }

    public int getEXTBreaksQuality() {
        return breaksQuality;
    }

    public int getEXTDrivingModes() {
        return drivingModes;
    }

    public int getEXTTransmission() {
        return transmission;
    }
}
