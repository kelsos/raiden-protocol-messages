from eth_utils import decode_hex, encode_hex
from raiden.messages.abstract import SignedMessage
from raiden.messages.matrix import ToDevice
from raiden.messages.metadata import Metadata, RouteMetadata
from raiden.messages.transfers import LockExpired, Unlock, RefundTransfer, Lock, LockedTransfer
from raiden.messages.withdraw import WithdrawRequest, WithdrawConfirmation, WithdrawExpired
from raiden.storage.serialization import JSONSerializer
from raiden.utils.signer import LocalSigner

private_key = decode_hex('0x0123456789012345678901234567890123456789012345678901234567890123')
signer = LocalSigner(private_key)


def print_information(message: SignedMessage):
    print(f'{message.__class__}')
    packed = message._data_to_sign()
    signature = signer.sign(packed)

    if hasattr(message, 'message_hash'):
        print(f'message hash: {encode_hex(message.message_hash)}')

    print(f'packed: {encode_hex(packed)}')
    print(f'signature: {encode_hex(signature)}')

    message.signature = signature

    print(f'message: {JSONSerializer.serialize(message)}')

    print('\n---------------------------\n')


locked_transfer = LockedTransfer(
    chain_id=337,
    message_identifier=123456,
    payment_identifier=1,
    nonce=1,
    token_network_address=decode_hex('0xe82ae5475589b828D3644e1B56546F93cD27d1a4'),
    token=decode_hex('0xc778417E063141139Fce010982780140Aa0cD5Ab'),
    channel_identifier=1338,
    transferred_amount=0,
    locked_amount=10,
    recipient=decode_hex('0x2A915FDA69746F515b46C520eD511401d5CCD5e2'),
    locksroot=decode_hex('0x607e890c54e5ba67cd483bedae3ba9da9bf2ef2fbf237b9fb39a723b2296077b'),
    lock=Lock(
        expiration=1,
        amount=10,
        secrethash=decode_hex('0x59cad5948673622c1d64e2322488bf01619f7ff45789741b15a9f782ce9290a8')
    ),
    target=decode_hex('0x811957b07304d335B271feeBF46754696694b09e'),
    initiator=decode_hex('0x540B51eDc5900B8012091cc7c83caf2cb243aa86'),
    fee=0,
    metadata=(Metadata(routes=[(RouteMetadata(
        route=[
            decode_hex('0x2A915FDA69746F515b46C520eD511401d5CCD5e2'),
            decode_hex('0x811957b07304d335B271feeBF46754696694b09e'),
        ]
    ))])),
    signature=''
)

refund_transfer = RefundTransfer(
    chain_id=337,
    message_identifier=123457,
    payment_identifier=1,
    nonce=1,
    token_network_address=decode_hex('0xe82ae5475589b828D3644e1B56546F93cD27d1a4'),
    token=decode_hex('0xc778417E063141139Fce010982780140Aa0cD5Ab'),
    channel_identifier=1338,
    transferred_amount=0,
    locked_amount=10,
    recipient=decode_hex('0x540B51eDc5900B8012091cc7c83caf2cb243aa86'),
    locksroot=decode_hex('0x0000000000000000000000000000000000000000000000000000000000000000'),
    lock=Lock(
        expiration=1,
        amount=10,
        secrethash=decode_hex('0x59cad5948673622c1d64e2322488bf01619f7ff45789741b15a9f782ce9290a8')
    ),
    target=decode_hex('0x540B51eDc5900B8012091cc7c83caf2cb243aa86'),
    initiator=decode_hex('0x2A915FDA69746F515b46C520eD511401d5CCD5e2'),
    fee=0,
    metadata=(Metadata(routes=[(RouteMetadata(
        route=[
            decode_hex('0x540B51eDc5900B8012091cc7c83caf2cb243aa86'),
        ]
    ))])),
    signature=''
)

unlock = Unlock(
    chain_id=337,
    message_identifier=123457,
    payment_identifier=1,
    secret=decode_hex('0x3bc51dd335dda4f6aee24b3f88d88c5ee0b0d43aea4ed25a384531ce29fb062e'),
    nonce=1,
    token_network_address=decode_hex('0xe82ae5475589b828D3644e1B56546F93cD27d1a4'),
    channel_identifier=1338,
    transferred_amount=0,
    locked_amount=10,
    locksroot=decode_hex('0x607e890c54e5ba67cd483bedae3ba9da9bf2ef2fbf237b9fb39a723b2296077b'),
    signature=''
)

lock_expired = LockExpired(
    chain_id=337,
    message_identifier=123457,
    nonce=1,
    token_network_address=decode_hex('0xe82ae5475589b828D3644e1B56546F93cD27d1a4'),
    channel_identifier=1338,
    transferred_amount=0,
    locked_amount=10,
    secrethash=decode_hex('0xfdd5831261497a4de31cb31d29b3cafe1fd2dfcdadf3c4a72ed0af9bb106934d'),
    locksroot=decode_hex('0x607e890c54e5ba67cd483bedae3ba9da9bf2ef2fbf237b9fb39a723b2296077b'),
    recipient=decode_hex('0x540B51eDc5900B8012091cc7c83caf2cb243aa86'),
    signature=''
)

to_device = ToDevice(
    message_identifier=123456,
    signature=''
)

withdraw_request = WithdrawRequest(
    signature='',
    nonce=135,
    token_network_address=decode_hex('0xe82ae5475589b828D3644e1B56546F93cD27d1a4'),
    participant=decode_hex('0x2A915FDA69746F515b46C520eD511401d5CCD5e2'),
    total_withdraw=10000000000000000000,
    message_identifier=123456,
    channel_identifier=1338,
    expiration=182811,
    chain_id=337,
)

withdraw_confirmation = WithdrawConfirmation(
    signature='',
    nonce=135,
    token_network_address=decode_hex('0xe82ae5475589b828D3644e1B56546F93cD27d1a4'),
    participant=decode_hex('0x2A915FDA69746F515b46C520eD511401d5CCD5e2'),
    total_withdraw=10000000000000000000,
    message_identifier=123456,
    channel_identifier=1338,
    expiration=182811,
    chain_id=337,

)

withdraw_expired = WithdrawExpired(
    signature='',
    nonce=135,
    token_network_address=decode_hex('0xe82ae5475589b828D3644e1B56546F93cD27d1a4'),
    participant=decode_hex('0x2A915FDA69746F515b46C520eD511401d5CCD5e2'),
    total_withdraw=10000000000000000000,
    message_identifier=123456,
    channel_identifier=1338,
    expiration=182811,
    chain_id=337,

)

# TODO add missing messages: Processed,Delivered,SecretRequest,SecretReveal

print_information(locked_transfer)
print_information(refund_transfer)
print_information(unlock)
print_information(lock_expired)
print_information(to_device)
print_information(withdraw_request)
print_information(withdraw_confirmation)
print_information(withdraw_expired)
