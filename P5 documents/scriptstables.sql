-- MySQL Script generated by MySQL Workbench
-- Mon Mar 11 09:44:30 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema pure_beurre
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema pure_beurre
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pure_beurre` DEFAULT CHARACTER SET utf8 ;
USE `pure_beurre` ;

-- -----------------------------------------------------
-- Table `pure_beurre`.`Category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pure_beurre`.`Category` (
  `idCategory` INT NOT NULL AUTO_INCREMENT,
  `name_category` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idCategory`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE UNIQUE INDEX `idCategory_UNIQUE` ON `pure_beurre`.`Category` (`idCategory` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `pure_beurre`.`Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pure_beurre`.`Product` (
  `idproduct` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `product_name` VARCHAR(100) NOT NULL,
  `nutriscore` VARCHAR(1) NOT NULL,
  `store` VARCHAR(100) NULL,
  `ingredients` LONGTEXT NULL,
  `url` VARCHAR(255) NOT NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`idproduct`, `category_id`),
  CONSTRAINT `fk_Product_Category1`
    FOREIGN KEY (`category_id`)
    REFERENCES `pure_beurre`.`Category` (`idCategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Product_Category1_idx` ON `pure_beurre`.`Product` (`category_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `pure_beurre`.`Substitute`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pure_beurre`.`Substitute` (
  `idsubstitute` INT NOT NULL AUTO_INCREMENT,
  `product_id` INT UNSIGNED NOT NULL,
  `previous_id` INT NOT NULL,
  PRIMARY KEY (`idsubstitute`, `product_id`),
  CONSTRAINT `fk_Substitute_Product1`
    FOREIGN KEY (`product_id`)
    REFERENCES `pure_beurre`.`Product` (`idproduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Substitute_Product1_idx` ON `pure_beurre`.`Substitute` (`product_id` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
