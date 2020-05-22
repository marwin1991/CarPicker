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

    private int enginePower; //KM 1 - 400
    private double fuelUsage; //l/100km
    private double acceleration; //0-100km in how much seconds
    private int maxSpeed; //km/h
    private int engineReliability = 5; // in scale from 1 to 10

    private int carFrontSpace; //1-10
    private int carBackSpace;// 1-10
    private int trunkSpace; // l
    private int comfort = 5; // in scale from 1 to 10

    private int finishQuality = 5;
    private int muteQuality = 5;
    private int easeOfUse = 5;

    private int comfortAdditionalEquipment;
    private int safetyAdditionalEquipment;
    private int otherAdditionalEquipment;

    private BigDecimal price = BigDecimal.valueOf(100000L);
    private BigDecimal priceDef = BigDecimal.valueOf(80000L);
    private BigDecimal additionalCosts = BigDecimal.valueOf(5000);


    private int drivingExpQuality; //1-10
    private int breaksQuality;// 1-10

    private int drivingModes = 5;
    private int transmission; //1-Manual, 5-All, 10-Auto


    public int getEnginePower() {
        return (enginePower * 10 / 400);
    }

    public int getFuelUsage() {
        return (int) (fuelUsage * 10 / 25);
    }

    public int getAcceleration() {
        return (int) (acceleration * 10 / 25);
    }

    public int getMaxSpeed() {
        return maxSpeed * 10 / 300;
    }

    public int getEngineReliability() {
        return engineReliability;
    }

    public int getCarFrontSpace() {
        return carFrontSpace;
    }

    public int getCarBackSpace() {
        return carBackSpace;
    }

    public int getTrunkSpace() {
        return trunkSpace * 10 / 500;
    }

    public int getComfort() {
        return comfort;
    }

    public int getFinishQuality() {
        return finishQuality;
    }

    public int getMuteQuality() {
        return muteQuality;
    }

    public int getEaseOfUse() {
        return easeOfUse;
    }

    public int getComfortAdditionalEquipment() {
        return comfortAdditionalEquipment;
    }

    public int getSafetyAdditionalEquipment() {
        return safetyAdditionalEquipment;
    }

    public int getOtherAdditionalEquipment() {
        return otherAdditionalEquipment;
    }

    public int getPrice() {
        return price.intValue() * 10 / 1000000;
    }

    public int getPriceDef() {
        try {
            return priceDef.divide(price).intValue() * 10;
        } catch (Exception e){
            return 0;
        }
    }

    public int getAdditionalCosts() {
        if(price != null && !price.equals(BigDecimal.ZERO))
            return additionalCosts.divide(price).intValue() * 10;
        return 0;
    }

    public int getDrivingExpQuality() {
        return drivingExpQuality;
    }

    public int getBreaksQuality() {
        return breaksQuality;
    }

    public int getDrivingModes() {
        return drivingModes;
    }

    public int getTransmission() {
        return transmission;
    }
}
