<p align="center"><img align="center" src="https://res.cloudinary.com/chaca-sa/image/upload/v1679027493/328169508_122397193933692_2960493904923070018_n_vxtlez.jpg" style="width: 300px"/></p>

# 🧑‍🦲 Proyecto "Pedro"

> ### ⚠️ Aclaración
> La estructura y repartición de tareas de este proyecto ha sido definido por Héctor a las 4 de la tarde mientras está escuchando el partido del Barcelona de fondo. Así que cualquier sugerencia se debe llevar a las organizaciones pertinentes (o sea los otros dos integrantes del equipo)

> ### 😹 Chistecillo
> - Mamá los fideos se están pegando en el sartén
> - No te metas, deja que se golpeen 

## 😀 Objetivos del trabajo
- Lograr que **Amaya** no deje espacios en blanco innecesarios
- Conseguir que **Hector** y **José** no cometan faltas de ortografía en los comentarios
- Aprobar Economía Empresarial **(opcional)**
- Mantener el nivel de sensualidad del equipo por las nubes

> ### 😹 Chistecillo
> El otro día vi un otaku triste y lo anime

## 🕛 Antes de empezar
> ### ⚠️ Aclaración
> **PyQt pesa mas de 60 MB así que cuidado no me denuncien**
- Abrir la consola Anaconda **(poner Anaconda Prompt en el buscador de Windows)**
- Crear un entorno virtual **en caso de no haber creado uno**
 
  ```bash
  conda create -n <nombre_entorno>
  ```

- Activar con **conda** el entorno virtual en caso de tenerlo
  
  ```bash
  conda activate <nombre_entorno>
  ```

- Instalar las librerías (`PyQt6`, `matplotlib`)

  ```bash
  pip install -r requirements.txt
  ```
  
> ### 😹 Chistecillo
> Por qué los pinareños llevan cubos de agua al estadio? Para hacer la ola
  
## 📚 Estructura (hasta ahora)

```bash
  |--- src
    |--- modules
      |--- file_reader
        |--- classes
        |--- services
      |--- graph
        |--- classes
        |--- services
      |--- views
        |--- Main_Window
          |--- controller.py
          |--- ui.py
  |--- test
      |--- graph
      |--- file
```

### Modules
La carpeta `modules` se refiere a los módulos o más bien las entidades de la aplicación. En este caso están `graph` y `file_reader`. **Todos los módulos deben tener las carpetas `classes` y `services`**.
- La carpeta `classes` se refiere a las clases necesarias para trabajar. El caso más fácil es el grafo que habría que crear por ejemplo las clases `GraphNode`, `Graph`, `GraphEdge`, etc.
- La carpeta `services` son los servicios del módulo. Por ejemplo para el `file_reader` se le pueden crear estos servicios

```python
class FileReaderServices:
    // lee el txt y devuelve un grafo a través de lo leído 
    def import_graph_txt(self) -> Graph:
        open('tengo_hambre.txt', encoding='utf-8')
        // resto de la lógica
    
    def export_graph_txt(self, graph: Graph):
        pass
```

### Views 
La carpeta `views` está destinada a contener las carpetas con cada ventana del proyecto. **(Lo más probable es que sea solo una que no vamos a hackear la NASA ni nada así)**.
- Cada vista debe tener dos archivos: un `controller` donde estará la lógica de la interfaz, y un `ui` que tiene todo el código de la interfaz **Donde no debe haber lógica practicamente**.

### Relación Vista-Controlador-Servicio
Para hacerme el inteligente voy a intentar explicar como se debería realizar cualquier procedimiento con esta relación. Como no se escribir voy a hacerlo a través de dibujos 
#### Esta seria una vista de forma general
<img src="https://res.cloudinary.com/chaca-sa/image/upload/v1682810720/VISTA_kltgja.png"/>

#### Esto sería un ejemplo
<img src="https://res.cloudinary.com/chaca-sa/image/upload/v1682810721/CONTROLLER_mg2flk.png"/>

### Test
La carpeta hasta ahora tiene dos sub-carpetas que pertenecen a cada módulo. En cada una de ellas deben ir los casos de test por separado con cada una de sus pruebas

#### Ejemplo
```bash
|--- file
  |--- import_graph_test.py
  |--- export_graph_test.py
  |--- incorrect_pattern_test.py
```

> ### 😹 Chistecillo
> Cuál es el vino más amargo? Vino mi suegra

## 💻 Tareas (por ahora)
### 🧑‍🚀 Tareas de José 
- ✅ Crear la lógica básica del grafo. O sea crear la clase `Graph`, `GraphEdge`, `GraphNode` con sus propiedades.
- ✅ Hacer el método dentro de `Graph` para poder hacer el recorrido a lo ancho. **Creo que lo mejor seria que devolviera un array con el nombre de cada nodo que recorre**
- ✅ Crear unos cuantos archivos `.txt` dentro de la carpeta `src/modules/file_reader/data` que sean datos de prueba para extraer grafos de ellos.
- ✅ Crear test que verifiquen que se está haciendo bien el recorrido a lo ancho.
- ⭕ Crear excepciones propias para cada caso de error que pueda devolver los procesos del grafo
- ⭕ Validar el formulario de los nodos (en `FormSection.update_gaph_section`), hay que mostrar un mensaje con la información del error en caso de que haya algún error **(ya está mas menos adelantado sólo hay que fijarse en lo que está hecho)** 

### 🐈 Tareas de Amaya 
- ⭕ Crear los métodos para importar y exportar en txt los grafos en `File_Reader_Services`.
- ⭕ Crear en `Graph` un método para recorrer en profundidad. **Creo que lo mejor seria que devolviera un array con el nombre de cada nodo que recorre**
- ⭕ Crear archivos txt dentro de la carpeta `src/modules/file_reader/data` (pueden ser con patrones erroneos).
- ⭕ Crear tests para verificar que se importa bien un grafo, y en caso de importarlo mal lanzar una excepción que se pueda identificar

### 🦍 Tareas de Héctor
- ⭕ Crear la interfaz del `Main_Window`.
- ⭕ Implementar los controladores dentro de las interfaces.
- ⭕ Crear en `Graph_Services` los métodos para insertar, eliminar y modificar los nodos de un grafo.
- ⭕ Crear la representación del grafo en la pantalla.

> ### 😹 Chistecillo
> Qué le dice una nariz a un pañuelo? Me zuenas

## 📜 Estructura de los txt (pendiente a revisión con el tribunal)
Lo mejor que se me llegó a ocurrir (Gracias a Lissandra) fue que se guarden en forma de matriz de adyacencia las relaciones definiendo las relaciones y darle valor a los pesos.

### Ejemplo
```text
A B C D

0 0 2 3
1 0 0 0
0 0 0 4
0 0 1 0
```

- La primera fila significa el nombre de cada uno de los nodos
- Después está una línea en blanco para separar la matriz de los nombres
- Viene después la matriz **que obviamente debe ser cuadrática con la misma cantidad de filas y de columnas que de nodos** 
- Cada uno de los valores representan el peso de la conexión **(Si es 0 significa que no existe conexión)**
- Los valores de la conexión también pueden ser strings

> ### 😹 Chistecillo
> Por qué el plátano no tiene dinero? Porque plata-no

## 🧪 Test
> ### ⚠️ Advertencia
> Poner `test` delante del nombre de cada método para que se detecte (no sean como yo que estuve 1 hora sin saber por qué no salía)

```python
import unittest


# se declara la clase y se dice que herede de `unittest.TestCase` para indicar que es un caso de test
class TestSum(unittest.TestCase):
    # cada método de test debe estar con la palabra test delante para que sea detectado
    def test_sum(self):
      realValue = sum([1, 2, 3])
      expectedValue = 6
      
      # Se espera que la suma del array de como resultado 6
      self.assertEqual(realValue, expectedValue, "Should be 6")

    # se pueden declarar tantos test cases como se quiera
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

# indica que cuando se llame a este archivo especificamente se ejecutaran todos los tests
if __name__ == '__main__':
    unittest.main()
```

### Llamar al test
Hay que ir a la terminal y poner:
```bash
python test/nombre_carpeta/<nombre_archivo>.py
```
En nuestro caso por ejemplo:
```bash
python test/file/import_graph_test.py
```
**Pycharm puede ejecutarlo de distintas formas hasta con distintas interfaces pero ya hay que buscar como se hace especificamente**

### Links para ver más cosas de `unitest`
- [https://www.digitalocean.com/community/tutorials/python-unittest-unit-test-example](https://www.digitalocean.com/community/tutorials/python-unittest-unit-test-example)
- [https://realpython.com/python-testing/](https://realpython.com/python-testing/)
- [https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/](https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/)
