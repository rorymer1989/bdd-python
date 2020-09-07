@web
Feature: Validar Menssage en el Browser

    Scenario: Valid Message
        Given Open Browser Chrome
         When Validar mensaje
         Then Salir del Browser