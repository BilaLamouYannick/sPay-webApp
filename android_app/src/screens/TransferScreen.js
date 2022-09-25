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
} from 'react-native';
import { TextInput } from 'react-native-gesture-handler';
import {useSafeAreaInsets} from 'react-native-safe-area-context';
import Ionicons from '@expo/vector-icons/Ionicons';
import axios from 'axios';
import { SERVER_URL } from '../consts/serverURL';


const baseUrl = SERVER_URL;
  

  const requete = (amount,receiver_cart_number, cart_number,email, password) => {
    
    const response =  axios.post(`${baseUrl}/api/v_1/transfert/`, {
      amount,
      receiver_cart_number,
      cart_number,
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
        // navigation.navigate('Home', {
        //   user: response.data.user, transactions: response.data.transactions, wallet: response.data.wallet
        // })
        // setVerification(true)
        console.log(response.data)
        ToastAndroid.show(" success ", ToastAndroid.SHORT)
        //navigation.navigate('Wallet')
        //{console.log(response.status)}
          //{console.log(response.data.user)}
      }
    ).catch( error=>{
      ToastAndroid.show(" Error ", ToastAndroid.SHORT)
      console.log(error)
  
    }); 
  }


const Transfer = ({route}) => {
  const insets = useSafeAreaInsets();

  const [layouts, setLayout] = React.useState(null);

  const navigation = useNavigation();

  const [receiverCardNumber, onChangeReceiverCardNumber] = React.useState(null);
  const [pass, onChangePass] = React.useState(null);
  const [amount, onChangeAmount] = React.useState(null);
  const [verification,setVerification] = React.useState(true)

  return (
    <View style ={{flex: 1, backgroundColor:'#131313',marginTop: 20, justifyContent: 'center'}}>
    <Text style={styles.textTitle}> Init a new Transfer </Text>
    <View style = {{height: 300, width: '90%', backgroundColor:'#b8b2b2', borderRadius:10,alignSelf:'center', alignItems:'center',justifyContent:'center'}}>
    {/* <TextInput 
            onChangeText={onChangeAmount}
            value={amount}
            placeholder={'Amont'}
            placeholderTextColor={'#b8b2b2'}
            style={{height:50, width:'90%', backgroundColor:'#131313', borderRadius:10,marginTop:5, color:'#FFF', fontSize:15, fontWeight:'bold'}}>
        </TextInput> */}
         <View style={{height:50 ,flexDirection:'row', alignItems:'center', backgroundColor:'#131313',borderRadius:10,fontstyle: 'bold', width:'90%'}}>
        <Ionicons name="pricetags-sharp" size={32} color="#b8b2b2" />
          <TextInput
        style={styles.input}
        onChangeText={onChangeAmount}
        value={amount}
        keyboardType='numeric'
        placeholder={'Amont'}
        placeholderTextColor={'#b8b2b2'}
      />
      {console.log(amount)}
        </View>
        {/* <TextInput 
            onChangeText={onChangeReceiverCardNumber}
            value={receiverCardNumber}
            placeholder={'Spay receiver Number'}
            placeholderTextColor={'#b8b2b2'}
            keyboardType='numeric'
            style={{height:50, width:'90%', backgroundColor:'#131313', borderRadius:10,marginTop:5, color:'#FFF', fontSize:15, fontWeight:'bold'}}>
        </TextInput>
        {console.log(receiverCardNumber)} */}
         <View style={{height:50 ,flexDirection:'row', alignItems:'center', backgroundColor:'#131313', margin: 12,borderRadius:10,fontstyle: 'bold', width:'90%'}}>
        <Ionicons name="card" size={32} color="#b8b2b2" />
          <TextInput
        style={styles.input}
        onChangeText={onChangeReceiverCardNumber}
        value={receiverCardNumber}
        keyboardType='numeric'
        placeholder={'Spay receiver Number'}
        placeholderTextColor={'#b8b2b2'}
      />
      {console.log(receiverCardNumber)}
        </View>
        {/* <TextInput 
            onChangeText={onChangePass}
            value={pass}
            placeholder={'Confirm with your password'}
            placeholderTextColor={'#b8b2b2'}
            secureTextEntry={true} 
            style={{height:50, width:'90%', backgroundColor:'#131313', borderRadius:10, marginTop:5, marginBottom: 5,color:'#FFF', fontSize:15, fontWeight:'bold'}}>
        </TextInput>
        {console.log(pass)} */}
        <View style={{height:50 ,flexDirection:'row', alignItems:'center', backgroundColor:'#131313', borderRadius:10,fontstyle: 'bold', width:'90%'}}>
        <Ionicons name="lock-closed" size={32} color="#b8b2b2" />
          <TextInput
        style={styles.input}
        onChangeText={onChangePass}
        value={pass}
        placeholder={'Confirm with your password'}
        placeholderTextColor={'#b8b2b2'}
        secureTextEntry={true} 
      />
      {console.log(pass)}
        </View>
    </View>
    <View>
            <TouchableOpacity
              style={styles.button}
              onPress={() => 
              // verification?ToastAndroid.show("Transfer success ", ToastAndroid.SHORT) :ToastAndroid.show("Transfer error ", ToastAndroid.SHORT) 
              amount!=null && receiverCardNumber!=null &&  pass!=null && requete(amount,receiverCardNumber, route.params.wallet.cart_number, route.params.user.email, pass)
            }>
              
              <Text style={styles.buttonText}>Init</Text>
            </TouchableOpacity>
        </View>
        {/* {console.log(route.params.wallet)} */}
    </View>
   
  );
};

export default Transfer;

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
    marginBottom: 40
  },
  button: {
    backgroundColor: '#FFF',
    paddingHorizontal: 30,
    paddingVertical: 12,
    borderRadius: 100,
    width:200,
    alignSelf:'center',
    marginTop:60

  },
  buttonText: {
    fontSize: 16,
    fontWeight: '700',
    textAlign:'center'
  },
  input: {
    // height: 40,
    // margin: 12,
    // borderWidth: 1,
    // padding: 10,
    // borderColor: '#FFF',
    // fontWeight: 'bold',
    // color:'#FFF'
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
