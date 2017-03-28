*** Settings ***
Documentation     Teste de validacao do Arduino Zabbix Agent 1.0.
Resource          resource.txt

*** Variables ***

*** Test Cases ***
First Zabbix Test
    Test
    Result should be  Zabbix Test

Test command ping
    Send Command        agent.ping
    Result should be    pong

Test command version
    Send Command        agent.version
    Result should be    Arduino Zabbix Agent 0.1

Test command temperatura
    Send Command        agent.temp
    Result in range     0.0  99.0

Test command umidade
    Send Command        agent.umid
    Result in range     0.0  99.0

Test command ethernet
    Send Command        agent.ethernet
    Result in range     0  4

Test command falha range
    Send Command        agent.umid
    Result in range     80  90

Test command close
    Send Command        agent.close
    Result should be    closed
    Close Connection

Test command invalid
    Send Command        agent.invalido
    Result should be    Invalid command