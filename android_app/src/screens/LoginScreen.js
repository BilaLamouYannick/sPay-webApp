import {useNavigation} from '@react-navigation/core';
import React from 'react';
import {
  StyleSheet,
  Text,
  View,
  ImageBackground,
  Image,
  TouchableOpacity,
  ActivityIndicator,
  ToastAndroid,
  Linking
} from 'react-native';
import { TextInput } from 'react-native-gesture-handler';
import {useSafeAreaInsets} from 'react-native-safe-area-context';
import Ionicons from '@expo/vector-icons/Ionicons';
import { SERVER_URL, } from '../consts/serverURL';

import axios from 'axios'
 const baseUrl = SERVER_URL;
import {DataConsumerHook} from '../Store'

let donnee
 export const testContext = React.createContext(donnee);
  const requete = (mail, pass) => {
    const response =  axios.post(`${baseUrl}/api/v_1/login/`, {
      email,
      password
    },
    {
      headers:{
        // 'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    }).then(
      response =>{
        allData= response.data
        DAT = response.data
        navigation.navigate('Home', {
          user: response.data.user, transactions: response.data.transactions, wallet: response.data.wallet
        })
        ToastAndroid.show(" success ", ToastAndroid.SHORT)
        //{console.log(response.status)}
          //{console.log(response.data.user)}
      }
    ).catch( error=>{
      ToastAndroid.show("Error: bad information ", ToastAndroid.SHORT)
      console.log(error)
  
    });
  
  }


const Login = () => {
 
  const [data, dispatch] = DataConsumerHook();
  const setContext = (dat)=> {
    dispatch({
        type: 'setData',
         dat
    });
}

  // fetch(`${baseUrl}/api/v_1/login/`, {
  // method: 'POST',
  // headers: {
  //   Accept: 'application/json',
  //   'Content-Type': 'application/json'
  // },
  //   body: JSON.stringify({
  //     "email": email,
  //     "password": password
  //   })
  // });


  
  
  const insets = useSafeAreaInsets();

  const [layouts, setLayout] = React.useState(null);

  const navigation = useNavigation();

  const [mail, onChangeMail] = React.useState(null);
  const [pass, onChangePass] = React.useState(null);


  //const [verification,setVerification] = React.useState(false)


  const email=mail
  const password= pass
  let allData = [] 
  
  const req= ()=>{

    const response =  axios.post(`${baseUrl}/api/v_1/login/`, {
    email,
    password
  },
  {
    headers:{
      // 'Accept': 'application/json',
      'Content-Type': 'application/json'
    }
  }).then(
    response =>{
      allData= response.data
      donnee= response.data
      setContext(response.data)
      console.log(data)

      navigation.navigate('Home', {
        user: response.data.user, transactions: response.data.transactions, wallet: response.data.wallet
      })
      ToastAndroid.show(" success ", ToastAndroid.SHORT)
      //{console.log(response.status)}
        //{console.log(response.data.user)}
    }
  ).catch( error=>{
    ToastAndroid.show("Error: bad information ", ToastAndroid.SHORT)
    console.log(error)

  });

  
  return response.status
}

// const transition = () => {
//   const req = req()
//   if (req == 200){
//     ToastAndroid.show("success ", ToastAndroid.SHORT)
//     navigation.navigate('Home')
//   }
//   else{
//     ToastAndroid.show("Error: bad information ", ToastAndroid.SHORT)
//   }
// } 

  return (
    <ImageBackground
      source={require('../assets/bg_welcome.png')}
      style={[styles.container, {paddingTop: insets.top}]}>
    <View style={styles.wrapper}>
        <View >
            <Text style={styles.textTitle}> Log In </Text>
        </View>
        <View style = {{height: 250, width: '90%', backgroundColor:'#0a0a0a', borderRadius:10,alignSelf:'center', alignItems:'center',justifyContent:'center'}}>
        <View style={{flexDirection:'row', alignItems:'center', margin: 12,borderWidth: 2,borderRadius:10,borderColor: '#FFF',fontstyle: 'bold', width:'90%'}}>
        <Ionicons name="mail" size={32} color="#FFF" />
          <TextInput
        style={styles.input}
        onChangeText={onChangeMail}
        value={mail}
        placeholder={'Mail'}
        placeholderTextColor={'#b8b2b2'}
      />
      {console.log(mail)}
        </View>
        <View style={{flexDirection:'row', alignItems:'center', margin: 10,borderWidth: 2,borderRadius:10,borderColor: '#FFF',fontstyle: 'bold', width:'90%'}}>
        <Ionicons name="lock-closed" size={32} color="#FFF" /> 
      <TextInput
        style={styles.input}
        onChangeText={onChangePass}
        value={pass}
        placeholder={'Password'}
        placeholderTextColor={'#b8b2b2'}
        secureTextEntry={true} 
      />
      {console.log(pass)}
      </View>
      </View>
        <View>
            <TouchableOpacity
              style={styles.button}
             onPress={() => req()}>
              <Text style={styles.buttonText}>Login</Text>
            </TouchableOpacity>
            <View style={{flexDirection:'row', alignItems:'center', alignSelf:'center'}}>
               <Text style={styles.escape}>Don't have any account?</Text>
               <TouchableOpacity onPress={() => Linking.openURL(`${baseUrl}/accounts/signup/personal/`)}>
                  <Text style={{  textAlign:'center',color:'#FFF',fontSize: 15, marginTop: 15}}> Sign Up</Text>
              </TouchableOpacity>
            </View>
           
        </View>
      </View>
    </ImageBackground>
    
  );
  
};

{/*onPress={() => verification?navigation.navigate('Home'):console.log("error of verification")}*/}
export default Login
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
  },
  textTitle:{
    alignSelf: 'center',
    color:'#FFF',
    fontWeight:'bold',
    fontSize:30,
    marginBottom: 10
  },
  button: {
    backgroundColor: '#FFF',
    paddingHorizontal: 30,
    paddingVertical: 12,
    borderRadius: 100,
    width:200,
    alignSelf:'center',
    marginTop:30

  },
  buttonText: {
    fontSize: 16,
    fontWeight: 'bold',
    textAlign:'center'
  },
  input: {
    height: 40,
    width:'85%',
    marginLeft: 12,
    padding: 10,
    borderColor: '#FFF',
    fontWeight: 'bold',
    color:'#FFF'
  },
  escape:{
    textAlign:'center',
    color:'#FFF',
    fontSize: 13,
    marginTop: 15

  },
});
