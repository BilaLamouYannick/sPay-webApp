import {useNavigation} from '@react-navigation/core';
import React from 'react';
import SelectDropdown from 'react-native-select-dropdown';
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
import { Picker } from '@react-native-picker/picker';
import Ionicons from '@expo/vector-icons/Ionicons';
import { SERVER_URL } from '../consts/serverURL';
import axios from 'axios';

  const operators= ["Orange","MTN"]

  const baseUrl = SERVER_URL;
  

  const requete = (amount, email, receiver_number, password, cart_number, operator) => {
    
    const response =  axios.post(`${baseUrl}/api/v_1/withdraw/`, {
      amount,
      email,
      receiver_number,
      password,
      cart_number,
      operator
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



  const Withdraw = ({route}) => {
  const insets = useSafeAreaInsets();

  const [layouts, setLayout] = React.useState(null);

  const navigation = useNavigation();

  const [pass, onChangePass] = React.useState(null);
  const [amount, onChangeAmount] = React.useState(null);
  const [withdrawalNumber,onChangeWithdrawalNumber] = React.useState(null);
  const [selectedValue,setSelectedValue] = React.useState("MTN");
  const [verification,setVerification] = React.useState(true)

  return (
    <View style ={{flex: 1, backgroundColor:'#131313', justifyContent: 'center'}}>
    <Text style={styles.textTitle}> Withdraw </Text>
    <View style = {{height: 300, width: '90%', backgroundColor:'#b8b2b2', borderRadius:10,alignSelf:'center', justifyContent:'center'}}>
    {/* <TextInput 
            onChangeText={onChangeAmount}
            value={amount} 
            placeholder={'Withdrawal amount'}
            placeholderTextColor={'#b8b2b2'}
            style={{height:50, width:'90%', backgroundColor:'#131313', alignSelf:'center',borderRadius:10,marginTop:5, color:'#FFF', fontSize:15, fontWeight:'bold'}}>
        </TextInput>
        {console.log(amount)} */}
        <View style={{height:50 ,flexDirection:'row', alignItems:'center', backgroundColor:'#131313', borderRadius:10,fontstyle: 'bold', width:'90%', alignSelf: 'center'}}>
        <Ionicons name="pricetags-sharp" size={32} color="#b8b2b2" />
          <TextInput
        style={styles.input}
        onChangeText={onChangeAmount}
        value={amount}
        keyboardType='numeric'
        placeholder={'Withdrawal amount'}
        placeholderTextColor={'#b8b2b2'}
      />
      {console.log(amount)}
        </View>
        {/* <TextInput 
            onChangeText={onChangeWithdrawalNumber}
            value={withdrawalNumber} 
            keyboardType='numeric'
            placeholder={'+237 xxx xxx xxx'}
            placeholderTextColor={'#b8b2b2'}
            style={{height:50, width:'90%', backgroundColor:'#131313',alignSelf:'center', alignSelf:'center',borderRadius:10,marginTop:5, color:'#FFF', fontSize:15, fontWeight:'bold'}}>
        </TextInput>
        {console.log(withdrawalNumber)} */}
        <View style={{height:50 ,flexDirection:'row', alignItems:'center', backgroundColor:'#131313', margin: 12,borderRadius:10,fontstyle: 'bold', width:'90%',alignSelf: 'center'}}>
        <Ionicons name="card" size={32} color="#b8b2b2" />
          <TextInput
        style={styles.input}
        onChangeText={onChangeWithdrawalNumber}
        value={withdrawalNumber}
        keyboardType='numeric'
        placeholder={'+237 xxx xxx xxx'}
        placeholderTextColor={'#b8b2b2'}
      />
      {console.log(withdrawalNumber)}
        </View>
        {/* <TextInput 
            onChangeText={onChangePass}
            value={pass} 
            placeholder={'Confirm with your password'}
            placeholderTextColor={'#b8b2b2'}
            secureTextEntry={true}
            style={{height:50, width:'90%', backgroundColor:'#131313',alignSelf:'center', borderRadius:10, marginTop:5, marginBottom: 5,color:'#FFF', fontSize:15, fontWeight:'bold'}}>
        </TextInput>
        {console.log(pass)} */}
        <View style={{height:50 ,flexDirection:'row', alignItems:'center', backgroundColor:'#131313', borderRadius:10,fontWeight: 'bold', width:'90%',alignSelf: 'center'}}>
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
        {console.log(route.params.wallet)}
        {/*<SelectDropdown
	data={operators}
	onSelect={(selectedItem, index) => {
		console.log(selectedItem, index)
        
	}}
	buttonTextAfterSelection={(selectedItem, index) => {
		return selectedItem
	}}
	rowTextForSelection={(item, index) => {
		return item
	}}
/>*/} 
<Picker
selectedValue={selectedValue}
style={{ height: 50, width: 150 ,}}
onValueChange={(itemValue, itemIndex) => setSelectedValue(itemValue)}
>
<Picker.Item label="MTN" value="MTN" />
<Picker.Item label="Orange" value="Orange" />
</Picker>
{console.log(selectedValue)}
    </View>
    <View>
            <TouchableOpacity
              style={styles.button}
              onPress={() => 
              //verification?ToastAndroid.show("Withdraw success ", ToastAndroid.SHORT) :ToastAndroid.show("Withdraw error ", ToastAndroid.SHORT) 
              amount!=null && withdrawalNumber!=null &&  pass!=null &&selectedValue!=null && requete(amount,route.params.user.email, withdrawalNumber,pass,route.params.wallet.cart_number, selectedValue)}>
              <Text style={styles.buttonText}>Withdraw</Text>
            </TouchableOpacity>
        </View>
    </View>
   
  );
};

export default Withdraw;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
  },
  textTitle:{
    alignSelf: 'center',
    color:'#131313',
    fontWeight:'bold',
    fontSize:30,
    backgroundColor:'#FFF',
    marginBottom: 40,
    borderBottomRightRadius: 15,
    borderBottomLeftRadius: 15,
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
    // fontFamily: 'bold',
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
