//Este archivo Java Script pertenece a la pantalla de inicio de sesión de la aplicación JewelApp

import React from "react";//importamos react
import {Text, View, StyleSheet, Image, Button, Alert, StatusBar, TouchableOpacity, TextInput} from "react-native";//importamos algunos componentes desde react native
import logo from './assets/JewelAppIconFondoBlanco.png' //importamos el icono de JewelApp desde la carpeta assets

//creamos un componente llamado App
const App = () => {
//retornamos un componente View con el estilo container de la constante styles
    const [Usuario, onChangeUsu] = React.useState(null);
    const [Contraseña, onChangeContra] = React.useState(null);
    return (
    //etiqueta Image dentro del componente View con el estilo logo de la constante styles
    //etiqueta TouchableOpacity dentro del componente View con su color, texto, accion cuando se presiona
    //etiqueta TextInput dentro del componente View con su estilo y mensaje
    //etiqueta StatusBar dentro del componente View con su color y valor
    <View style={styles.container}>
<View style={styles.appBar}>
        <Text style={styles.textAppBar}>Iniciar sesión en Jewel App</Text>
      </View>
      <View style={{height:10}}>
                         </View>
    <StatusBar
            animated={true}
            backgroundColor="#00796B"
           />
        <Image
                source={logo}
                style={styles.logo}
                />
 <TextInput
        style={styles.input}
        onChangeText={onChangeUsu}
        placeholder="Usuario o correo"
        value={Usuario}
      />
       <TextInput
              style={styles.input}
              onChangeText={onChangeContra}
              placeholder="Contraseña"
              value={Contraseña}
            />
                <TouchableOpacity
                 onPress={() => Alert.alert('Botón ingresar presionado')}//Cuando se presiona aparece un componente Alert
                 style={styles.button}
>
                        <Text style={styles.buttonText}>Ingresar</Text>
                      </TouchableOpacity>
                      <Text></Text>
                <Text>o</Text>
                <TouchableOpacity
                 onPress={() => Alert.alert('Botón iniciar sesión con Facebook presionado')}//Cuando se presiona aparece un componente Alert
                 style={{backgroundColor:"#3b5998", padding: 10, marginTop: 13}}
>
                        <Text style={styles.buttonText}>Iniciar sesión con Facebook</Text>
                    </TouchableOpacity>
                <TouchableOpacity
                  onPress={() => Alert.alert('Botón iniciar sesión con Google presionado')}//Cuando se presiona aparece un componente Alert
                  style={{backgroundColor:"#4285F4", padding: 10, marginTop: 13}}
                  >
                        <Text style={styles.buttonText}>Iniciar sesión con Google</Text>
                    </TouchableOpacity>
                    <Text></Text>
                    <Text></Text>
                    <Text>¿No tienes cuenta?</Text>
                    <TouchableOpacity
                                     onPress={() => Alert.alert('Botón registrarse presionado')}//Cuando se presiona aparece un componente Alert
                                     style={{backgroundColor:"#FFFFFF", padding: 10, marginTop: 5}}
                    >
                                            <Text style={{color: "#1976D2",  fontWeight: "bold", textDecorationLine: 'underline'}}>Registrarse</Text>
                                        </TouchableOpacity>
                     <View style={{height:40}}>
                     <Text></Text>
                               </View>
    </View>
);
};

const styles = StyleSheet.create({
//se agrupan multiples estilos creando un objeto tipo StyleSheet dentro de una constante llamada styles
    container: { flex: 1, justifyContent: 'center', alignItems: 'center' , backgroundColor: "#FFFFFF"},
    //se centra horizontal y verticalmente
    title: {fontSize: 50, color: "#FFFFFF",  fontWeight: "bold", fontFamily: "montserrat"},
    //se define el tamaño de la letra
    logo: {height: 150, width: 150, borderRadius: 0},
    //se define el alto y ancho del logo
    button: {backgroundColor:"#FFC107", padding: 10, marginTop: 13},
    //se define el color, la margen y el padding del boton
    buttonText: {color: "#FFFFFF", fontSize: 15},
    //se define el color y el tamaño de la letra del boton
   input: {
       height: 40,
       width: 300,
       margin: 15,
       padding: 10,
       borderWidth: 1,
     },
     appBar:{
     alignItems: "center",
     backgroundColor: "#009688",
     padding: 20,
     width: 360,
     },
     textAppBar:{
     color: "#FFFFFF",
     fontSize: 20,
     fontWeight: "bold",
     },
    });

export default App;
//exportamos el componente App