//Este archivo Java Script pertenece a la pantalla Cargando de la aplicación JewelApp

import React from "react";//importamos react
import {Text, View, StyleSheet, Image} from "react-native";//importamos algunos componentes desde react native
import logo from './assets/IconoJewelApp.png' //importamos el icono de JewelApp desde la carpeta assets

//creamos un componente llamado App
const App = () => {
//retornamos un componente View con el estilo container de la constante styles
    return (
    //etiqueta Image dentro del componente View con el estilo logo de la constante styles
    <View style={styles.container}>
        <Image
                source={logo}
                style={styles.logo}
                />
    </View>
);
};

const styles = StyleSheet.create({
//se agrupan multiples estilos creando un objeto tipo StyleSheet dentro de una constante llamada styles
    container: { flex: 1, justifyContent: 'center', alignItems: 'center' , backgroundColor: "#D8D8D8"},
    //se centra horizontal y verticalmente
    title: {fontSize: 50, color: "#FFFFFF"},
    //se define el tamaño de la letra
    logo: {height: 250, width: 250, borderRadius: 0},
    //se define el alto y ancho del logo

    });

export default App;
//exportamos el componente App