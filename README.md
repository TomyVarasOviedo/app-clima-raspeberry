# Proyecto: Clima Raspberry
> El circuito consiste de 4 secciones, Una computadora central, una unidad de procesamiento, placa controlador, y el display. La computadora central está compuesta de una Raspberry Pi 3 b+, con la que se accedera a una API utilizando internet para conseguir el clima de la zona actual, también está contara con un sistema de relojes, que permitirá poner alarmas, temporizadores, cronómetros y mostrar la hora actual. Esta información es luego enviada a la unidad de procesamiento. La unidad de procesamiento consiste de un Arduino Uno con un AtMega328, este se encargará de recibir la información de la computadora central, y modificarla de tal manera, que esta pueda ser recibida por la placa controladora. La placa controladora consiste de una placa de circuito impreso, con un Conversor BCD a Display, para que la información la unidad de procesamiento sea más eficiente, la información transmitida por la misma se encontrara en BCD (binary coded decimal), para ocupar menos espacio en placa. Finalmente el display consistirá en un Display LCD 2x16, con el que podremos mostrar hasta 32 caracteres alfanuméricos que serán enviados desde la computadora central.
> # Comando de inicializacion
> ```bash
>    uvicorn main:app --reload --port #### --host ####
> ```
