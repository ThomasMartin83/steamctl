from steam.enums.base import SteamIntEnum

class EPaymentMethod(SteamIntEnum):
    NONE = 0
    ActivationCode = 1
    CreditCard = 2
    Giropay = 3
    PayPal = 4
    Ideal = 5
    PaySafeCard = 6
    Sofort = 7
    GuestPass = 8
    WebMoney = 9
    MoneyBookers = 10
    AliPay = 11
    Yandex = 12
    Kiosk = 13
    Qiwi = 14
    GameStop = 15
    HardwarePromo = 16
    MoPay = 17
    BoletoBancario = 18
    BoaCompraGold = 19
    BancoDoBrasilOnline = 20
    ItauOnline = 21
    BradescoOnline = 22
    Pagseguro = 23
    VisaBrazil = 24
    AmexBrazil = 25
    Aura = 26
    Hipercard = 27
    MastercardBrazil = 28
    DinersCardBrazil = 29
    AuthorizedDevice = 30
    MOLPoints = 31
    ClickAndBuy = 32
    Beeline = 33
    Konbini = 34
    EClubPoints = 35
    CreditCardJapan = 36
    BankTransferJapan = 37
#   PayEasyJapan = 38 removed "renamed to PayEasy"
    PayEasy = 38
    Zong = 39
    CultureVoucher = 40
    BookVoucher = 41
    HappymoneyVoucher = 42
    ConvenientStoreVoucher = 43
    GameVoucher = 44
    Multibanco = 45
    Payshop = 46
#   Maestro = 47 removed "renamed to MaestroBoaCompra"
    MaestroBoaCompra = 47
    OXXO = 48
    ToditoCash = 49
    Carnet = 50
    SPEI = 51
    ThreePay = 52
    IsBank = 53
    Garanti = 54
    Akbank = 55
    YapiKredi = 56
    Halkbank = 57
    BankAsya = 58
    Finansbank = 59
    DenizBank = 60
    PTT = 61
    CashU = 62
    AutoGrant = 64
    WebMoneyJapan = 65
    OneCard = 66
    PSE = 67
    Exito = 68
    Efecty = 69
    Paloto = 70
    PinValidda = 71
    MangirKart = 72
    BancoCreditoDePeru = 73
    BBVAContinental = 74
    SafetyPay = 75
    PagoEfectivo = 76
    Trustly = 77
    UnionPay = 78
    BitCoin = 79
    Wallet = 128
    Valve = 129
#   SteamPressMaster = 130 removed "renamed to MasterComp"
    MasterComp = 130
#   StorePromotion = 131 removed "renamed to Promotional"
    Promotional = 131
    MasterSubscription = 134
    Payco = 135
    MobileWalletJapan = 136
    OEMTicket = 256
    Split = 512
    Complimentary = 1024
    Unknown = 1025

class EPackageStatus(SteamIntEnum):
    Available = 0
    Preorder = 1
    Unavailable = 2
    Invalid = 3

