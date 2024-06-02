# Tema 2.2: Módulos de Marketing y Ventas
## Arquitecturas de los SI:
- Arquitectura Técnica: organización en vista, modelo de negocio, persistencia.
- Arquitectura Funcional: organizacion por módulos:
    * Marketing y Ventas
    * Producción y Cadena de Suministro

##  Proceso de Ventas:
- Presupuesto y órdenes de venta: Departamento de ventas
- Despacho de las ordenes: Almacen o Producción
- Facturacion de las ordenes: Contabilidad y facturacion
- Cobro/Devolución de ordenes: Contabilidad y facturación + Almacen

### Problemas actuales en el proceso de ventas
- Precio incorrecto
- Se llama muchas veces a los clientes para solicitarles información
- Retrasos en el procesamiento de las órdenes
- No se cumple con los plazos de entrega

### Origenes de los problemas en le proceso de ventas
- La compania distintos SI para cada area funcional:
    * SI de Ventas
    * SI de Almacen
    * SI de Contabilidad
- La información almacenada en esos sistemas no esta disponible en tiempo real.
- Un número elevado de transacciones se realizan de forma manual

## Presupuestos y órdenes de venta
El vendedor le da al cliente interesado un presupuesto:
- El contacto se realiza mediante una llamada telefónica o
mediante una visita comercial directa.
- Al final del proceso de venta el vendedor genera un presupuesto escrito a mano, del que se generan tres copias:
    * El original se lo queda el cliente.
    * La primera copia se envía por fax o correo a la oficina de ventas.
    * La segunda copia se la queda el vendedor para su propio registro.

El cliente interesado en hacer el pedido según lo
presupuestado, llama por teléfono al departamento de
ventas de la compañía.

### Problemas en presupuestos y órdenes de venta
- Determinación de la fecha de entrega del producto:
    * El vendedor no conoce en tiempo real el stock, los
planes de producción ni otras ventas realizadas.
- Comprobación del nivel de crédito del cliente:
    * El departamento de ventas no conoce en tiempo real
las facturas que tiene pendientes el cliente ni los pagos
que ha realizado.
- Entrada de la orden del cliente en el SI:
    * Al ser un proceso manual lleva tiempo y puede
introducir multitud de errores.

## Despacho de las órdenes de venta
- Listas de empaquetado y etiquetas de envío:
    * Se imprimen dos veces al día.
- Se llevan manualmente al almacén.
- Se ordenan manualmente en el almacén para diferenciar entre órdenes grandes y pequeñas.
- Se realiza el proceso de empaquetado en dos áreas
separadas del almacén según el tamaño de la orden.
- Se emplea un programa en un ordenador personal para gestionar el nivel de inventario del almacén.
    * Finalizadas las órdenes hay que reducir el nivel de inventario.

## Proceso de empaquetado
El empleado encargado de procesar una orden entra en el almacén
para coger los elementos que forman parte del producto.
- La compañía, debido a que trabaja con productos perecederos mantiene un nivel muy bajo de stock:
    * Los niveles de stock cambian muy rápidamente.
- No es raro que al llegar a las estanterías del almacén nos encontremos con que no hay suficiente mercancía para completar el pedido.
    * En ese caso, el empleado debe hablar con varias personas para decidir qué hacer con el producto:
        - Jefe del almacén: por si tenemos previsto recibir producto.
        - Jefe de producción: por si están fabricando producto que esté disponible en breve.
        - Agentes de ventas: por si se puede reducir el pedido o retrasar.

## Contabilidad y facturación
- Los agentes de ventas envían los pedidos a
contabilidad para que se haga la facturación de
los mismos.
- El personal de contabilidad introduce
manualmente los datos en sus SI.
- En el caso de que los agentes de ventas tengan que hacer ajustes en los pedidos, se envía una orden de correccion a contabilidad.

### Problemas de facturación
- El proceso de entrada de datos para generar las facturas es manual:
    * Lento.
        - Las facturas llegan más tarde de lo que debería:
            * ¡Tardamos en cobrar los pedidos!

    * Expuesto a errores humanos.
- Las correciones a los pedidos se han de procesar también de froma manual:
    * Mismos problemas.
- En ocasiones las correcciones no se realizan antes de la emisión de facturas:
    * Las facturas que se le envían a los clientes son erróneas.
        - La imagen de la empresa se ve deteriorada.
        - Solventar estos problemas requiere un proceso adicional que lleva tiempo.
            * Más retrasos de cara al cliente.
            * ¡Tardamos en cobrar los pedidos!

## Pagos y devoluciones
- Una vez recibida la mercancía, el cliente:
    * Realiza el pago
    * Realiza devolución:
        + Por algun motivo el pedido no es correcto o no está en buen estado.
        + Como los productos son perecederos, el cliente puede devolversol cuando los recibe a punto de caducar.
    * Para realizar una devolución, hay que enviar la mercancía e informacion sobre el pedido.
        + Concretamente la referencia RMA (Return Merchandise Authorization)

### Problemas con los pagos y devoluciones
- Los problemas en la caligrafía de la documentación que se envía pueden dificultar el ingreso de la información en el sistema.
- La mayor parte de los clientes olvidan especificar el RMA de la devolución.
    * Esto dificulta al departamento de contabilidad localizar la cuenta donde habrá que incrementar el crédito.
        + Lleva más tiempo y esfuerzo.
        + El cliente puede ver sus nuevos pedidos bloqueados por falta de crédito cuando en realidad no necesita pagar nada.
        + El cliente puede recibir una carta de reclamación del pago cuando en realidad no le corresponde.
            - Mala imagen de la compañía.

## Ventas y distribución en un ERP
- Los ERPs ofrecen ventajas frente a los SI tradicionales:
    * Minimiza los errores en la entrada de datos.
        + Los datos sólo se introducen una vez en el sistema.
        + En la mayoría de los casos actuales, los datos vienen directamente de la fuente: Vendedor o directamente el cliente.

    * Ofrece información actualizada a los usuarios:
        + Tenemos toda la información disponible a la hora de hacer un pedido. P. ej.: Precios, fechas de entrega, ...

    * Tenemos un registro centralizado de todas las transacciones relativas a cada pedido:
        + Pedido.
        + Modificaciones del pedido.
        + Facturas.
        + RMAs

## Tratamiento de las ventas en un ERP
- El ERP trata las ventas como un ciclo de eventos:
    * Actividades de pre-venta.
    * Procesamiento de las órdenes de venta.
    * Acomodación de inventario.
    * Entrega.
    * Facturación.
    * Pago.

### Actividades de pre-venta
- Ofrecer precio de los productos a los clientes:
    * Mediante consultas o presupuestos.
- Actividades de marketing:
    * P. ej. Seguimiento de clientes: Control de llamadas,visitas, envíos de correo promocional (mailings), ....

- Recolección de datos de clientes y clientes potenciales:
    * La compañía puede segmentar la cartera de clientes y oportunidades por sus datos para realizar tareas de marketing más efectivas.

### Procesamiento de las órdenes de venta
- Secuencia de actividades que deben producirse para registrar una venta:
    * Introducir la orden de venta en el sistema.
    * Comprobar crédito del cliente:
        + Si el cliente tiene suficiente crédito:
            - Cerrar la orden de venta.
        + Si el cliente no tiene suficiente crédito:
            - Avisar al personal de ventas para que se tomen las acciones adecuadas:
                * Revisar crédito.
                * Aceptar / Rechazar orden.

### Orden de venta
- Pueden basarse en un presupuesto que se haya generado en la fase de pre-venta.
    * La información del presupuesto del sistema se emplea automáticamente como datos de las órdenes de venta.
    * No es necesario duplicar la entrada de datos.
- Al procesar una orden de venta es crítico establecer:
    * Los productos que compra el cliente.
    * La cantidad de los productos.
    * El precio de los productos: No es una tarea obvia.
        + Puede haber diversas alternativas para establecer precios.

### Acomodación de inventario
- Comprobar que podemos suministrar el producto en la fecha de entrega establecida:
    * El ERP debe consultar los registros de la gestión de almacén y de producción para determinar si la mercancía está disponible en los almacenes:
        + La tenemos en stock.
        + La tendremos fabricada a tiempo.
    * Hay que incluir el tiempo que llevará el envío de los productos.

- En función de los datos anteriores, el sistema puede recomendar a fabricación un incremento en la producción.

### Entrega
- El sistema ERP generará los documentos necesarios para:
    * Recogida en almacén de los productos.
    * Empaquetado de los productos.
    * Envío de los productos.
- Puede planificar las actividades anteriores para que sean más eficientes:
    * P. ej. Unir envíos a un mismo cliente. Aprovechar la recogida de productos para una venta con los de otra venta, ...

### Facturación
- El sistema ERP generará la factura empleando los datos de la orden de venta:
    * Evitamos introducir los datos de nuevo:
        + Reducimos errores.
        + Reducimos tiempo de facturación.

- El personal de contabilidad puede imprimir las facturas y enviarlas por correo o fax.
    * Se puede automatizar el envío cuando se hace por medios electrónicos (fax, email, ...).

- El ERP actualiza automáticamente los registros de contabilidad.

### Pago
- Cuando el cliente hace el pago, éste puede ser procesado automáticamente por el ERP.
    * Formularios electrónicos.
    * Conexión con bancos.
- La rapidez con la que se procesan los pagos tienen una incidencia directa con el nivel de crédito del cliente:
    * Evitamos bloquearle órdenes a buenos clientes.
        + Mayor volumen de negocio.
        + Evitamos mala imagen de la compañía.

# CRMs
- Los CRMs (Costumer Relationship Management) son un tipo de SI para gestionar la relación de una compañía con sus clientes.
    * La idea es mejorar y optimizar las relaciones con los clientes.

- Sus funciones fundamentales:
    * Marketing personalizado (one-to-one)
    * Gestion de campañas de ventas
    * Automatización de call centers

## Beneficios de los CRMs
- Bajos costes:
    * Se pueden implantar incluso "bajo demanda" contratando por tiempo el uso de un SI externo
- Mejora la estrategia de ventas y la valoracion del rendimiento
- Alto beneficio:
    * Dados los bajos costes y las mejoras, proporciona un entorno de inversion rápido.

## Resumen

- En la gestión de marketing y ventas, los SI integrados pueden optimizar los procesos de negocio.
- El uso de un ERP automatiza el procesamiento de las ordenes de venta.
- El uso de CRM optimiza la gestión y las estrategias de ventas de una compañía.
