import {useNavigation} from '@react-navigation/core';
import React from 'react';
import { ScrollView } from 'react-native-gesture-handler';
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
//import RecentTransaction from '../components/RecentTransaction';
import renderTransactionItem from '../components/RecentTransaction';
import { LastTransactions } from '../components/RecentTransaction';
import Card from '../components/Card'
 import testContext from '../screens/LoginScreen'



const listTransations = [
    {
      type: 'Spotify',
      icon: require('../assets/ic_spotify.png'),
      date: 'Jun 12, 12:30',
      payment: '+ $12',
    },
    {
      type: 'Paypal',
      icon: require('../assets/ic_paypal.png'),
      date: 'Jun 12, 15:40',
      payment: '+ $12',
    },
    {
      type: 'Dribble',
      icon: require('../assets/ic_dribble.png'),
      date: 'Mai 29, 07:18',
      payment: '+ $50',
    },
    {
      type: 'Other1',
      icon: require('../assets/ic_dribble.png'),
      date: 'Mai 27, 10:37',
      payment: '+ $400',
    },
    {
      type: 'Other2',
      icon: require('../assets/ic_dribble.png'),
      date: 'Mai 19, 09:45',
      payment: '+ $500',
    },
    {
      type: 'Other3',
      icon: require('../assets/ic_dribble.png'),
      date: 'Mai 16, 15:55',
      payment: '+ $100',
    },
    {
        type: 'Other3',
        icon: require('../assets/ic_dribble.png'),
        date: 'Avr 30, 11:32',
        payment: '+ $238',
      },
      {
        type: 'Other3',
        icon: require('../assets/ic_dribble.png'),
        date: 'Avr 28, 08:43',
        payment: '+ $1000',
      },
  ];

const Wallet = ({route}) => {
  const insets = useSafeAreaInsets();

  const [layouts, setLayout] = React.useState(null);

  const navigation = useNavigation();
  const [ballance] = React.useState("19983848")

  //const [mail, onChangeMail] = React.useState("Your mail");
  //const [pass, onChangePass] = React.useState('Pass');

  const [verification,setVerification] = React.useState(true)
  return (
    <View style ={{flex: 1, backgroundColor:'#131313',paddingTop: 20, paddingRight: 10, paddingLeft:10}}>
      {/* {console.log(testContext.user)} */}
    <View style={{ alignContent: 'center', alignSelf:'flex-end', backgroundColor: '#FFF', borderRadius: 50, marginTop: 9, marginRight: 15}}>
    <TouchableOpacity onPress={() => navigation.navigate('Notification')}>
         <Image source={require('../assets/ic_notif.png')} color={'#FFF'} />
   </TouchableOpacity>
   </View>
   <View style={{ alignItems:'center'}}>
        <Card cardNumber={route.params.wallet.cart_number} cardHolder={route.params.user.first_name} cardName={route.params.user.email}/>
    </View>
    <Text style={{color:'#FFF'}}>Your Ballance</Text>
    <View style = {{height: 40, width: '60%', backgroundColor:'white', borderBottomRightRadius:20,borderTopRightRadius:20,  flexDirection:'row',}}>
        <Image source= {require('../assets/ic_wallet.png')} style ={{ alignSelf:'center'}}/>
        <Text style ={{ alignSelf:'center', marginLeft: 5, fontSize: 15, fontWeight:'bold'}}> {route.params.wallet.balance} FCFA </Text>
    </View>
    <Text style={{marginTop:10, marginBottom:10 ,alignSelf:'center', color:'#FFF', fontSize:10,fontWeight:'bold',}}>Recent Transactions </Text>
    {/* <ScrollView>
        {listTransations.map(renderTransactionItem)}
    </ScrollView> */}
    <ScrollView>
        <LastTransactions transactions= {route.params.transactions} user= {route.params.user}/>
    </ScrollView>
    {console.log(route.params.transactions)}
    {console.log(route.params.wallet)}
    </View>
    
  );
};

export default Wallet;

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
    marginTop:100

  },
  buttonText: {
    fontSize: 16,
    fontWeight: '700',
    textAlign:'center'
  },
  input: {
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
    borderColor: '#FFF',
    fontFamily: 'bold',
    color:'#FFF'
  },
  escape:{
    textAlign:'center',
    color:'#FFF',
    fontSize: 13,
    marginTop: 15

  },
});
